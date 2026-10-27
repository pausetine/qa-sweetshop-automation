
from playwright.sync_api import expect
from tests.helpers import shop_page, add_product


def test_guest_add_to_basket(page):
    # Open sweets page without logging in
    shop_page(page)

    # Add Chocolate Cups
    add_product(page, "Chocolate Cups")

    # Open basket using the actual website navigation
    # This selector must be verified in DevTools first
    page.get_by_role(
        "link", name="Basket"
    ).click()

    # Check if Chocolate Cups appears
    expect(
        page.get_by_text("Chocolate Cups", exact=True)
    ).to_be_visible()
