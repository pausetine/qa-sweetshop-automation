"""Cart and shipping: includes assertions intended to reveal planted defects."""

import pytest
from playwright.sync_api import expect
from tests.helpers import add_product, basket_page, page_text, shop_page


@pytest.mark.boundary
def test_TC_BAS_001_empty_basket_total_zero(page):
    basket_page(page)
    expect(
        page.locator('a[href="/basket"] .badge')
    ).to_have_text("0")


@pytest.mark.positive
def test_TC_BAS_002_added_product_appears_in_basket(page):
    # Open the product catalog
    shop_page(page)

    # Confirm basket is empty initially
    basket_badge = page.locator(
        'a.nav-link[href="/basket"] .badge'
    )

    expect(basket_badge).to_have_text("0")

    # Add Sherbert Fountain
    add_product(page, "Sherbert Fountain")

    # Wait until the basket badge updates
    expect(basket_badge).to_have_text("1")

    # Open basket through website navigation
    basket_page(page)

    # Check the selected product appears
    expect(
        page.get_by_text("Sherbert Fountain", exact=True)
    ).to_be_visible()

@pytest.mark.positive
@pytest.mark.positive
def test_TC_BAS_003_two_products_have_correct_subtotal(page):
    # Allow extra time for website navigation
    page.set_default_navigation_timeout(30000)

    shop_page(page)

    basket_badge = page.locator(
        'a[href="/basket"] .badge'
    )

    expect(basket_badge).to_have_text("0")

    # Add Sherbert Fountain (£0.35)
    add_product(page, "Sherbert Fountain")
    expect(basket_badge).to_have_text("1")

    # Add Sherbert Straws (£0.75)
    add_product(page, "Sherbert Straws")
    expect(basket_badge).to_have_text("2")

    basket_page(page)

    # Check both products
    expect(
        page.get_by_text("Sherbert Fountain", exact=True)
    ).to_be_visible()

    expect(
        page.get_by_text("Sherbert Straws", exact=True)
    ).to_be_visible()

    # Expected subtotal: £0.35 + £0.75 = £1.10
    assert "£1.10" in page_text(page)


@pytest.mark.boundary
def test_TC_BAS_004_collect_shipping_is_free(page):
    shop_page(page)

    basket_badge = page.locator(
        'a[href="/basket"] .badge'
    )

    add_product(page, "Sherbert Fountain")
    expect(basket_badge).to_have_text("1")

    print("BEFORE NAVIGATION:", basket_badge.inner_text())

    basket_page(page)

    print("AFTER NAVIGATION:", page_text(page))

    # Check product is still in basket
    expect(
        page.get_by_text(
            "Sherbert Fountain", exact=True
        )
    ).to_be_visible()

    # Select free collection
    page.get_by_text("Collect (FREE)", exact=True).click()

    print("AFTER FREE COLLECTION:", page_text(page))

    # Check product remains visible
    expect(
        page.get_by_text(
            "Sherbert Fountain", exact=True
        )
    ).to_be_visible()

    # Verify the final price
    assert "£0.35" in page_text(page)
    assert "NaN" not in page_text(page)



@pytest.mark.positive
def test_TC_BAS_005_standard_shipping_adds_1_99(page):
    shop_page(page)

    basket_badge = page.locator(
        'a[href="/basket"] .badge'
    )

    add_product(page, "Sherbert Fountain")
    expect(basket_badge).to_have_text("1")

    basket_page(page)

    # Confirm product exists before shipping selection
    expect(
        page.get_by_text(
            "Sherbert Fountain", exact=True
        )
    ).to_be_visible()

    print("BEFORE SHIPPING:", page_text(page))

    # Select standard shipping
    page.locator(
        'label[for="exampleRadios2"]'
    ).click()

    expect(
        page.locator("#exampleRadios2")
    ).to_be_checked()

    print("AFTER SHIPPING:", page_text(page))

    # Verify product remains in the basket
    expect(
        page.get_by_text(
            "Sherbert Fountain", exact=True
        )
    ).to_be_visible()

    # £0.35 + £1.99 = £2.34
    assert "£2.34" in page_text(page)
    assert "NaN" not in page_text(page)


@pytest.mark.negative
def test_TC_BAS_006_empty_promo_cannot_redeem(page):
    basket_page(page)
    page.get_by_role("button", name="Redeem").click()
    expect(page.get_by_text("Please input a valid promo code.")).to_be_visible()
