# BUG-BAS-001: Standard Shipping Causes Basket Total to Display £NaN

- **Status:** Reproduced
- **Linked test case:** TC-BAS-005 (`tests/test_basket.py::test_TC_BAS_005_standard_shipping_adds_1_99`)
- **Date reproduced:** 2026-10-27
- **Tester:** Faustine
- **Environment:** Windows, Chromium (exact version not recorded), Python 3.13.3, Pytest 9.1.1, Playwright 1.64.1, 1280 × 900 viewport
- **URL:** https://sweetshop.vivrichards.co.uk/basket
- **Severity:** High — Incorrect order totals affect checkout reliability.
- **Priority:** P1 — Important purchasing functionality.
- **Preconditions:** Guest user with one Sherbert Fountain (£0.35) added to the basket.

## Steps to reproduce

1. Navigate to the Sweets page.
2. Add one Sherbert Fountain (£0.35) to the basket.
3. Open the Basket page.
4. Confirm the basket contains one product and displays a total of £0.35.
5. Select **Standard Shipping (£1.99)**.
6. Observe the updated Total (GBP).

## Expected result

The total should be £2.34 (£0.35 product subtotal + £1.99 shipping).

## Actual result

The total changes from £0.35 to `£NaN` after Standard Shipping is selected. The product remains in the basket.

## Reproducibility

1/1 documented successful execution of the shipping-selection flow reproduced this defect. Additional runs are recommended.

## Evidence

- **Screenshot:** `artifacts/screenshots/tests_test_basket.py_test_TC_BAS_005_standard_shipping_adds_1_99.png`
- **Test output:** Pytest FAILED, with `£NaN` appearing in the captured page text.
- **Console/network:** Not separately captured.

## Impact and notes

The basket displays an invalid monetary total when Standard Shipping is selected. This may confuse customers and could interfere with checkout if the invalid total is used downstream.

**Suspected cause:** An error in the JavaScript shipping calculation or numeric conversion. The specific cause has not yet been verified.

**Suggested fix:** Inspect the shipping calculation and ensure valid numeric values are used.

**Retest criteria:** Selecting Standard Shipping should produce £2.34 without displaying `NaN`.