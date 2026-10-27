"""Small shared page helpers; keep user-facing behavior in the tests."""

import re

from playwright.sync_api import expect


def shop_page(page):
    page.goto("/sweets", wait_until="domcontentloaded")
    expect(page.get_by_role("heading", name="Browse sweets")).to_be_visible()


def product_section(page, name):
    # The closest ancestor with an 'Add to Basket' action scopes the product.
    # If markup changes, fix this helper rather than individual test cases.
    heading = page.get_by_role("heading", name=name, exact=True)
    return heading.locator(
        "xpath=ancestor::*[.//*[normalize-space()='Add to Basket']][1]"
    )



def add_product(page, name):
    product_names = {
        "Sherbert Discs": "Sherbet Discs"
    }

    data_name = product_names.get(name, name)

    page.locator(
        f'a.addItem[data-name="{data_name}"]'
    ).click()



def basket_page(page):
    # Open the home page if the browser starts blank
    if page.url == "about:blank":
        page.goto("/", wait_until="domcontentloaded")

    # Click the actual Basket navigation link
    page.locator('a.nav-link[href="/basket"]').click()

    # Verify the Basket page opened
    expect(page).to_have_url(re.compile(r"/basket/?$"))

    expect(
        page.get_by_role(
            "heading",
            name=re.compile("Your Basket", re.I)
        ).first
    ).to_be_visible()


def page_text(page):
    return page.locator("body").inner_text()
