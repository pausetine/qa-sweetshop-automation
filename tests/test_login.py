"""Positive and negative login scenarios using site's publicly documented demo accounts."""

import re
import pytest
from playwright.sync_api import expect


def login_page(page):
    page.goto("/login")
    expect(page.get_by_role("heading", name="Login")).to_be_visible()


def log_in(page, email, password):
    page.get_by_placeholder("you@example.com").fill(email)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()


@pytest.mark.positive
@pytest.mark.parametrize(
    "email",
    ["oneorder@sweetshop.local", "twoorders@sweetshop.local", "fiveorders@sweetshop.local"],
    ids=["one-order", "two-orders", "five-orders"],
)
def test_TC_LOG_001_documented_demo_accounts_can_login(page, email):
    login_page(page)
    log_in(page, email, "qwerty")
    expect(page).not_to_have_url(re.compile(r"/login/?(?:\?.*)?$"))


@pytest.mark.negative
def test_TC_LOG_002_missing_email_rejected(page):
    login_page(page)
    page.get_by_placeholder("Password").fill("qwerty")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(re.compile(r"/login/?(?:\?.*)?$"))


@pytest.mark.negative
@pytest.mark.parametrize("email", ["not-an-email", "a@"], ids=["no-at", "missing-domain"])
def test_TC_LOG_003_bad_email_format_rejected(page, email):
    login_page(page)
    email_input = page.get_by_placeholder("you@example.com")
    email_input.fill(email)
    assert not email_input.evaluate("el => el.checkValidity()"), "Email should fail HTML validation"


@pytest.mark.negative
def test_TC_LOG_004_missing_password_rejected(page):
    login_page(page)
    page.get_by_placeholder("you@example.com").fill("oneorder@sweetshop.local")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(re.compile(r"/login/?(?:\?.*)?$"))



@pytest.mark.negative
def test_TC_LOG_005_wrong_password_rejected(page):
    login_page(page)

    log_in(
        page,
        "oneorder@sweetshop.local",
        "wrong-password"
    )

    # Incorrect credentials must not grant account access
    expect(
        page.get_by_role(
            "heading",
            name="Your Account"
        )
    ).not_to_be_visible()

    # User should remain on login page
    expect(page).to_have_url(
        re.compile(r"/login/?(?:\?.*)?$")
    )

