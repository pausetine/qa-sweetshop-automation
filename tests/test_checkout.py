"""Checkout validation only: tests never submit complete payment details."""

import re
import pytest
from playwright.sync_api import expect
from tests.helpers import basket_page


@pytest.mark.negative
def test_TC_CHK_001_empty_checkout_does_not_complete_order(page):
    basket_page(page)
    page.get_by_role("button", name="Confirm Order").click()
    expect(page).to_have_url(re.compile(r"/basket/?(?:\?.*)?$"))


@pytest.mark.negative
def test_TC_CHK_002_missing_email_is_invalid(page):
    basket_page(page)
    email_input = page.get_by_placeholder("you@example.com")
    email_input.fill("")
    assert not email_input.evaluate("el => el.checkValidity()"), "Billing email should be required"


@pytest.mark.boundary
def test_TC_CHK_003_bad_postcode_format_is_rejected(page):
    basket_page(page)
    postcode = page.get_by_placeholder("SW1A 1AA")
    postcode.fill("!")
    # A one-character punctuation string should not be accepted as a UK postcode.
    # This can surface missing validation in the deliberately buggy app.
    assert not postcode.evaluate("el => el.checkValidity()"), "UK postcode format not validated"



@pytest.mark.negative
@pytest.mark.parametrize(
    "value",
    ["!", "123", "ABCDE", "SW1A@1AA"],
    ids=["symbol", "numbers", "letters", "special-character"]
)
def test_TC_CHK_004_invalid_postcodes_rejected(page, value):
    basket_page(page)

    postcode = page.locator("#zip")
    postcode.fill(value)

    assert not postcode.evaluate(
        "el => el.checkValidity()"
    ), f"Invalid postcode accepted: {value}"


@pytest.mark.negative
@pytest.mark.parametrize(
    "value",
    ["not-an-email", "a@", "plainaddress"],
    ids=["missing-at", "missing-domain", "plain-text"]
)
def test_TC_CHK_005_invalid_billing_emails_rejected(page, value):
    basket_page(page)

    email = page.get_by_placeholder("you@example.com")
    email.fill(value)

    assert not email.evaluate(
        "el => el.checkValidity()"
    ), f"Invalid email accepted: {value}"



@pytest.mark.negative
def test_TC_CHK_006_empty_first_name_rejected(page):
    basket_page(page)

    # Both first and last name use id="name"
    # Select the first matching element
    first_name = page.locator('input#name').nth(0)

    expect(first_name).to_be_visible()

    # Leave first name empty
    first_name.fill("")

    # Verify required field validation
    assert not first_name.evaluate(
        "el => el.checkValidity()"
    ), "First name should be required"
