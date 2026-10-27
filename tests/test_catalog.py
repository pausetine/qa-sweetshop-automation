"""Catalog presence and product-price boundaries."""

import pytest
from playwright.sync_api import expect
from tests.helpers import product_section, shop_page


@pytest.mark.positive
def test_TC_CAT_001_catalog_shows_key_products(page):
    shop_page(page)
    for name in ("Chocolate Cups", "Sherbert Straws", "Sherbert Discs", "Dolly Mixture"):
        expect(page.get_by_role("heading", name=name, exact=True)).to_be_visible()


@pytest.mark.positive
@pytest.mark.parametrize(
    "name,price",
    [("Chocolate Cups", "£1.00"), ("Sherbert Straws", "£0.75"), ("Sherbert Discs", "£0.95")],
    ids=["chocolate-cups", "sherbert-straws", "sherbert-discs"],
)
def test_TC_CAT_002_price_matches_listed_product(page, name, price):
    shop_page(page)
    expect(product_section(page, name)).to_contain_text(price)


@pytest.mark.positive
def test_TC_CAT_003_catalog_has_add_actions(page):
    shop_page(page)
    assert page.get_by_text("Add to Basket", exact=True).count() >= 16


@pytest.mark.boundary
def test_TC_CAT_004_cheapest_listed_product_price(page):
    shop_page(page)
    expect(product_section(page, "Bubbly")).to_contain_text("£0.10")


@pytest.mark.boundary
def test_TC_CAT_005_highest_listed_product_price(page):
    shop_page(page)
    expect(product_section(page, "Swansea Mixture")).to_contain_text("£1.50")
