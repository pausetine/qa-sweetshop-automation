# BUG-LOG-001: Invalid Password Grants Access to Demo Customer Account

- **Status:** Reproduced
- **Linked test case:** TC-LOG-005 (`tests/test_login.py::test_TC_LOG_005_wrong_password_rejected`)
- **Date reproduced:** 2026-10-27
- **Tester:** Faustine
- **Environment:** Windows, Chromium (exact version not recorded), Python 3.13.3, Playwright 1.64.1, Pytest 9.1.1, viewport 1280 × 900
- **Severity:** High (provisional; authentication validation failure)
- **Priority:** P1 (provisional)
- **Preconditions:** Fresh browser context, no authenticated session, publicly documented demo account available.

## Steps to reproduce

1. Navigate to `https://sweetshop.vivrichards.co.uk/login`.
2. Enter `oneorder@sweetshop.local` in the email field.
3. Enter `wrong-password` in the password field instead of the documented `qwerty`.
4. Click Login.
5. Observe the destination page and displayed customer information.

## Expected result

The application should reject incorrect credentials, prevent access to the customer account, and display an appropriate login error.

## Actual result

The application navigated to a customer account page despite the incorrect password.

The resulting page displayed the One Order Customer account, including previous order information, favourite sweet, and total spending.

## Reproducibility

1/1 documented automated execution reproduced the issue. Further repetition is recommended.

## Evidence

- **Screenshot:** `artifacts/screenshots/tests_test_login.py_test_TC_LOG_005_wrong_password_rejected.png`
- **Test output:** Pytest FAILED — expected `/login`, but navigated to a customer-specific `.html` page.
- **Account-page evidence:** Heading `Your Account` and customer order information.
- **Console/network:** Not separately captured.

## Impact and notes

The application appears to allow access to a demo customer account without validating the documented password correctly.

This presents a potential authentication-control weakness. The demonstrated impact is limited to the public practice account; access to non-demo accounts has not been established.

**Suggested fix:** Validate submitted credentials before granting access to account information. Ensure invalid passwords result in an authentication error.

**Retest criteria:** Incorrect passwords must not provide access to the customer account, while the documented valid credentials should continue to work.