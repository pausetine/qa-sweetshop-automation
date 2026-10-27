"""Independent Playwright browser sessions and failure screenshots.

No pytest-playwright plugin is required: these fixtures use Playwright's
Python sync API directly. The target site is never modified by the fixtures.
"""

import os
import re
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

BASE_URL = os.getenv("BASE_URL", "https://sweetshop.vivrichards.co.uk").rstrip("/")
PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def browser():
    browser_type = os.getenv("BROWSER", "chromium").strip().lower()
    if browser_type not in {"chromium", "firefox", "webkit"}:
        raise ValueError("BROWSER must be chromium, firefox or webkit")
    headless = os.getenv("HEADLESS", "1").lower() not in {"0", "false", "no"}
    with sync_playwright() as playwright:
        engine = getattr(playwright, browser_type)
        instance = engine.launch(headless=headless)
        yield instance
        instance.close()


@pytest.fixture()
def context(browser):
    instance = browser.new_context(
        base_url=BASE_URL,
        viewport={"width": 1280, "height": 900},
        locale="en-GB",
    )
    yield instance
    instance.close()


@pytest.fixture()
def page(context):
    instance = context.new_page()
    instance.set_default_timeout(10_000)
    yield instance
    instance.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    page_obj = item.funcargs.get("page")
    if not page_obj or page_obj.is_closed():
        return
    safe_test_name = re.sub(r"[^a-zA-Z0-9_.-]+", "_", item.nodeid)
    screenshot_path = PROJECT_ROOT / "artifacts" / "screenshots" / f"{safe_test_name}.png"
    screenshot_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        page_obj.screenshot(path=str(screenshot_path), full_page=True)
        report.sections.append(("Screenshot", str(screenshot_path.relative_to(PROJECT_ROOT))))
    except Exception as err:
        report.sections.append(("Screenshot capture failed", str(err)))
