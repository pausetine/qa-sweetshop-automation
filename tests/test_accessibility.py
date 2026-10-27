
"""HTML accessibility checks for Sweet Shop."""

import pytest
from playwright.sync_api import expect


@pytest.mark.accessibility
@pytest.mark.parametrize(
    "path",
    ["/login", "/basket"],
    ids=["login", "basket"]
)
def test_TC_A11Y_001_page_has_unique_html_ids(page, path):
    page.goto(path, wait_until="domcontentloaded")

    duplicate_ids = page.locator("[id]").evaluate_all(
        """elements => {
            const seen = new Set();
            const duplicates = new Set();

            for (const el of elements) {
                if (seen.has(el.id)) {
                    duplicates.add(el.id);
                }
                seen.add(el.id);
            }

            return [...duplicates];
        }"""
    )

    assert not duplicate_ids, (
        f"Duplicate HTML IDs found on {path}: "
        f"{duplicate_ids}"
    )


@pytest.mark.accessibility
def test_TC_A11Y_002_login_fields_have_accessible_names(page):
    page.goto("/login", wait_until="domcontentloaded")

    email = page.get_by_role(
        "textbox",
        name="Email address",
        exact=True
    )

    password = page.get_by_label(
        "Password",
        exact=True
    )

    expect(email).to_have_count(1)
    expect(email).to_be_visible()

    expect(password).to_have_count(1)
    expect(password).to_be_visible()
