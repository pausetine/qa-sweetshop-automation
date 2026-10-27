"""TC-NAV-001 ... TC-NAV-004"""

import re
import pytest
from playwright.sync_api import expect



@pytest.mark.positive
def test_TC_NAV_001_homepage_renders(page):
    page.set_default_navigation_timeout(30000)

    page.goto(
        "/",
        wait_until="domcontentloaded"
    )

    expect(
        page.get_by_role(
            "heading",
            name="Welcome to the sweet shop!"
        )
    ).to_be_visible()



@pytest.mark.positive
def test_TC_NAV_002_browse_link_opens_catalog(page):
    # Allow more time for navigation
    page.set_default_navigation_timeout(30000)

    # Wait for HTML to load, not every resource
    page.goto("/", wait_until="domcontentloaded")

    # Click the Browse Sweets link
    page.get_by_role(
        "link", name="Browse Sweets"
    ).click()

    # Verify navigation to catalog
    expect(page).to_have_url(
        re.compile(r"/sweets/?(?:\?.*)?$")
    )

    # Verify catalog heading
    expect(
        page.get_by_role(
            "heading", name="Browse sweets"
        )
    ).to_be_visible()


@pytest.mark.positive
def test_TC_NAV_003_about_describes_test_site(page):
    page.goto("/about")
    expect(page.get_by_role("heading", name="Sweet Shop Project")).to_be_visible()
    expect(page.get_by_text("An intentionally broken web application", exact=False)).to_be_visible()


@pytest.mark.positive
def test_TC_NAV_004_basket_route_opens(page):
    page.goto("/basket")
    expect(page.get_by_role("heading", name="Your Basket").first).to_be_visible()
