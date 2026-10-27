# BUG-CHK-001: Invalid UK Postcode Passes Native Form Validation

- **Status:** Reproduced (native validation); full checkout validation unverified
- **Linked test case:** TC-CHK-003 (`tests/test_checkout.py::test_TC_CHK_003_bad_postcode_format_is_rejected`)
- **Date reproduced:** 2026-10-27
- **Tester:** Faustine
- **Environment:** Windows, Chromium (exact version not recorded), Python 3.13.3, Playwright 1.64.1, Pytest 9.1.1, viewport 1280 × 900
- **Severity:** Low (native form-validation gap; downstream impact unverified)
- **Priority:** P2 (provisional)
- **Preconditions:** Basket page is accessible. No completed order or payment submission required.

## Steps to reproduce

1. Navigate to `https://sweetshop.vivrichards.co.uk/basket`.
2. Locate the Postcode field under Billing Address.
3. Enter `!` as the postcode.
4. Open Chrome Developer Tools.
5. Inspect the postcode input with `id="zip"`.
6. Run `document.querySelector("#zip").checkValidity()` in the Console.
7. Observe the returned validation result.

## Expected result

The postcode field should reject an incorrectly formatted UK postcode, such as `!`, through an appropriate validation mechanism.

## Actual result

The postcode field accepts `!` under native HTML constraint validation.

`checkValidity()` returns `true`.

The HTML element has `required` but no `pattern` attribute specifying a valid postcode format.

## Reproducibility

1/1 documented automated test execution detected the validation gap. HTML inspection independently confirms the absence of a native postcode pattern.

## Evidence

- **Screenshot:** `artifacts/screenshots/tests_test_checkout.py_test_TC_CHK_003_bad_postcode_format_is_rejected.png`
- **Test output:** Pytest FAILED — `AssertionError: UK postcode format not validated`
- **HTML evidence:** `<input type="text" class="form-control" id="zip" placeholder="SW1A 1AA" required="">`
- **Console evidence:** Native validation returns `true` for the invalid value `!`.
- **Video/network:** Not separately captured.

## Impact and notes

The postcode field lacks native HTML format validation. This may allow malformed postcode values to proceed through client-side validation unless additional JavaScript checks reject them.

The issue could affect address accuracy and delivery processing, but the website's complete checkout validation has not been tested.

**Suggested fix:** Implement appropriate UK postcode format validation using HTML constraints and/or JavaScript, supported by server-side validation.

**Retest criteria:** The value `!` must be rejected by the intended postcode validation mechanism while valid UK postcodes remain accepted.