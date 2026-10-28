# Sweet Shop — Test Case Documents (TCDs)

**Application:** https://sweetshop.vivrichards.co.uk  
**Framework:** Python · Playwright · Pytest  
**Execution context:** Windows · Chromium  
**Basis:** 41 collected test executions and latest shared full-suite run (32 PASS / 9 FAIL; 193.69 seconds).  
**Scope:** No payment transaction submitted; no comprehensive server-side security or accessibility audit.

> **Purpose:** Detailed test case documents (TCDs). Parameterized cases use the same case ID with distinct dataset labels. Steps describe the test intent based on the shared test descriptions and execution logs; exact fixture code and selectors remain authoritative in `tests/`. The 'actual results' summarize observations from the shared test run, not new live verification.

## Test case inventory

| Module | Executions | Passed | Failed |
|---|---:|---:|---:|
| Navigation | 4 | 4 | 0 |
| Catalog | 7 | 7 | 0 |
| Basket | 6 | 5 | 1 |
| Login | 8 | 7 | 1 |
| Checkout | 11 | 6 | 5 |
| Accessibility | 3 | 2 | 1 |
| Images | 1 | 0 | 1 |
| Guest basket | 1 | 1 | 0 |
| **Total** | **41** | **32** | **9** |

## Detailed Test Case Documents

## Navigation — 4 test executions

### TCD-001 — TC-NAV-001: Verify homepage renders
**Test case ID:** TC-NAV-001  
**Test type:** Positive / Functional  
**Source:** `tests/test_navigation.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** URL: /  

**Test steps**
1. Open the home page.
2. Locate the welcome heading.

**Expected result:** Welcome heading is visible.  
**Actual result:** Welcome heading visible; successful retest.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-002 — TC-NAV-002: Verify Browse Sweets navigation
**Test case ID:** TC-NAV-002  
**Test type:** Positive / Functional  
**Source:** `tests/test_navigation.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Home page  

**Test steps**
1. Open the home page.
2. Click the Browse Sweets link.
3. Check route and catalog heading.

**Expected result:** Navigates to /sweets; Browse sweets heading appears.  
**Actual result:** Navigation and heading assertions passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-003 — TC-NAV-003: Verify About page content
**Test case ID:** TC-NAV-003  
**Test type:** Positive / Functional  
**Source:** `tests/test_navigation.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** About page  

**Test steps**
1. Navigate to About.
2. Check the About heading and explanatory content.

**Expected result:** About heading and description are visible.  
**Actual result:** Heading and descriptive content found.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-004 — TC-NAV-004: Verify basket page accessible
**Test case ID:** TC-NAV-004  
**Test type:** Positive / Functional  
**Source:** `tests/test_navigation.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Basket page  

**Test steps**
1. Use basket navigation.
2. Verify current URL and basket heading.

**Expected result:** Basket page opens and heading displays.  
**Actual result:** Basket route and heading assertions passed.  
**Execution status:** **PASS**  
**Related defect:** —

## Catalog — 7 test executions

### TCD-005 — TC-CAT-001: Verify key catalog products displayed
**Test case ID:** TC-CAT-001  
**Test type:** Positive / Functional  
**Source:** `tests/test_catalog.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Expected four product names from test  

**Test steps**
1. Navigate to /sweets.
2. Check each expected product heading.

**Expected result:** All four expected product names displayed.  
**Actual result:** Assertions passed for expected names.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-006 — TC-CAT-002: Verify listed price — Chocolate Cups
**Test case ID:** TC-CAT-002  
**Test type:** Positive / Data-driven  
**Source:** `tests/test_catalog.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Product dataset: chocolate-cups  

**Test steps**
1. Navigate to /sweets.
2. Find the corresponding product.
3. Compare displayed price with test dataset.

**Expected result:** Listed price equals expected dataset price.  
**Actual result:** Price comparison passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-007 — TC-CAT-002: Verify listed price — Sherbert Straws
**Test case ID:** TC-CAT-002  
**Test type:** Positive / Data-driven  
**Source:** `tests/test_catalog.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Product dataset: sherbert-straws  

**Test steps**
1. Navigate to /sweets.
2. Find the corresponding product.
3. Compare displayed price with test dataset.

**Expected result:** Listed price equals expected dataset price.  
**Actual result:** Price comparison passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-008 — TC-CAT-002: Verify listed price — Sherbert Discs
**Test case ID:** TC-CAT-002  
**Test type:** Positive / Data-driven  
**Source:** `tests/test_catalog.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Product dataset: sherbert-discs  

**Test steps**
1. Navigate to /sweets.
2. Find the corresponding product.
3. Compare displayed price with test dataset.

**Expected result:** Listed price equals expected dataset price.  
**Actual result:** Price comparison passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-009 — TC-CAT-003: Verify catalog Add to Basket actions
**Test case ID:** TC-CAT-003  
**Test type:** Positive / Functional  
**Source:** `tests/test_catalog.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** 16 expected controls  

**Test steps**
1. Open /sweets.
2. Locate product Add to Basket controls.
3. Assert count meets test expectation.

**Expected result:** At least 16 add controls present.  
**Actual result:** Count assertion passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-010 — TC-CAT-004: Verify minimum listed price
**Test case ID:** TC-CAT-004  
**Test type:** Boundary  
**Source:** `tests/test_catalog.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Bubbly: £0.10  

**Test steps**
1. Open the catalog.
2. Find Bubbly.
3. Check its price.

**Expected result:** Bubbly is listed at £0.10.  
**Actual result:** Expected price found.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-011 — TC-CAT-005: Verify maximum listed price
**Test case ID:** TC-CAT-005  
**Test type:** Boundary  
**Source:** `tests/test_catalog.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Swansea Mixture: £1.50  

**Test steps**
1. Open the catalog.
2. Find Swansea Mixture.
3. Check its price.

**Expected result:** Swansea Mixture is listed at £1.50.  
**Actual result:** Expected price found.  
**Execution status:** **PASS**  
**Related defect:** —

## Basket — 6 test executions

### TCD-012 — TC-BAS-001: Verify empty basket state
**Test case ID:** TC-BAS-001  
**Test type:** Boundary / Functional  
**Source:** `tests/test_basket.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable. No items added.  
**Test data:** Empty session  

**Test steps**
1. Open basket page.
2. Check basket count and/or empty total per test assertion.

**Expected result:** Basket count is zero; no items selected.  
**Actual result:** Empty basket assertions passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-013 — TC-BAS-002: Verify one item added to basket
**Test case ID:** TC-BAS-002  
**Test type:** Positive / Functional  
**Source:** `tests/test_basket.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Sherbert Fountain, £0.35  

**Test steps**
1. Open catalog.
2. Add Sherbert Fountain.
3. Open basket.
4. Check product and price/badge.

**Expected result:** Product is present in basket at expected price.  
**Actual result:** Assertions passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-014 — TC-BAS-003: Verify subtotal with two different products
**Test case ID:** TC-BAS-003  
**Test type:** Positive / Calculation  
**Source:** `tests/test_basket.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Sherbert Fountain £0.35; Sherbert Straws £0.75  

**Test steps**
1. Open catalog.
2. Add one of each product.
3. Open basket.
4. Inspect calculated subtotal.

**Expected result:** Subtotal £1.10.  
**Actual result:** £1.10 assertion passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-015 — TC-BAS-004: Verify free collection calculation
**Test case ID:** TC-BAS-004  
**Test type:** Boundary / Calculation  
**Source:** `tests/test_basket.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Sherbert Fountain £0.35; collection  

**Test steps**
1. Add Sherbert Fountain.
2. Open basket.
3. Select collection.
4. Inspect total.

**Expected result:** Collection adds £0.00; total remains £0.35.  
**Actual result:** Expected total found.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-016 — TC-BAS-005: Verify standard shipping calculation
**Test case ID:** TC-BAS-005  
**Test type:** Positive / Calculation  
**Source:** `tests/test_basket.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Sherbert Fountain £0.35; shipping £1.99  

**Test steps**
1. Add Sherbert Fountain.
2. Open basket.
3. Select Standard Shipping.
4. Inspect basket total.

**Expected result:** Total £2.34 (£0.35 + £1.99), not NaN.  
**Actual result:** Incorrect total; earlier browser inspection showed £NaN.  
**Execution status:** **FAIL**  
**Related defect:** BUG-BAS-001

### TCD-017 — TC-BAS-006: Verify blank promotion code cannot redeem
**Test case ID:** TC-BAS-006  
**Test type:** Negative / Validation  
**Source:** `tests/test_basket.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Promotion code: empty string  

**Test steps**
1. Open basket.
2. Leave promo code empty.
3. Attempt redeem action.
4. Check validation/unchanged application behavior.

**Expected result:** Empty promo cannot be redeemed.  
**Actual result:** Assertions passed.  
**Execution status:** **PASS**  
**Related defect:** —

## Login — 8 test executions

### TCD-018 — TC-LOG-001: Verify valid demo login — one-order
**Test case ID:** TC-LOG-001  
**Test type:** Positive / Data-driven  
**Source:** `tests/test_login.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** oneorder@sweetshop.local; published demo password  

**Test steps**
1. Open login page.
2. Enter published demo account and password.
3. Submit.
4. Verify navigation away from login.

**Expected result:** Demo account login redirects away from login.  
**Actual result:** Redirect assertion passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-019 — TC-LOG-001: Verify valid demo login — two-orders
**Test case ID:** TC-LOG-001  
**Test type:** Positive / Data-driven  
**Source:** `tests/test_login.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** twoorders@sweetshop.local; published demo password  

**Test steps**
1. Open login page.
2. Enter published demo account and password.
3. Submit.
4. Verify navigation away from login.

**Expected result:** Demo account login redirects away from login.  
**Actual result:** Redirect assertion passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-020 — TC-LOG-001: Verify valid demo login — five-orders
**Test case ID:** TC-LOG-001  
**Test type:** Positive / Data-driven  
**Source:** `tests/test_login.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** fiveorders@sweetshop.local; published demo password  

**Test steps**
1. Open login page.
2. Enter published demo account and password.
3. Submit.
4. Verify navigation away from login.

**Expected result:** Demo account login redirects away from login.  
**Actual result:** Redirect assertion passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-021 — TC-LOG-002: Verify missing login email is rejected
**Test case ID:** TC-LOG-002  
**Test type:** Negative / Required  
**Source:** `tests/test_login.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Email empty; password supplied as required by test  

**Test steps**
1. Open login page.
2. Leave email blank.
3. Attempt form submission.

**Expected result:** Login submission blocked.  
**Actual result:** Submission-blocking assertion passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-022 — TC-LOG-003: Verify invalid login email — no-at
**Test case ID:** TC-LOG-003  
**Test type:** Negative / Data-driven  
**Source:** `tests/test_login.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** text without @  

**Test steps**
1. Open login page.
2. Enter invalid email format.
3. Check input validity.

**Expected result:** Native email validity rejects malformed address.  
**Actual result:** Invalid format rejected.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-023 — TC-LOG-003: Verify invalid login email — missing-domain
**Test case ID:** TC-LOG-003  
**Test type:** Negative / Data-driven  
**Source:** `tests/test_login.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** address missing domain  

**Test steps**
1. Open login page.
2. Enter invalid email format.
3. Check input validity.

**Expected result:** Native email validity rejects malformed address.  
**Actual result:** Invalid format rejected.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-024 — TC-LOG-004: Verify missing login password rejected
**Test case ID:** TC-LOG-004  
**Test type:** Negative / Required  
**Source:** `tests/test_login.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Valid-format email; empty password  

**Test steps**
1. Open login page.
2. Leave password empty.
3. Attempt submission.

**Expected result:** Login submission blocked.  
**Actual result:** Assertion passed.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-025 — TC-LOG-005: Verify incorrect login password rejected
**Test case ID:** TC-LOG-005  
**Test type:** Negative / Authentication  
**Source:** `tests/test_login.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** oneorder@sweetshop.local; incorrect password  

**Test steps**
1. Open login page.
2. Enter documented demo email with deliberately incorrect password.
3. Submit.
4. Inspect page for authenticated account content.

**Expected result:** Incorrect password does not display an authenticated account.  
**Actual result:** Your Account page displayed despite incorrect password.  
**Execution status:** **FAIL**  
**Related defect:** BUG-LOG-001

## Checkout Validation — 11 test executions

### TCD-026 — TC-CHK-001: Verify entirely empty checkout cannot complete
**Test case ID:** TC-CHK-001  
**Test type:** Negative / Required  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Checkout form empty  

**Test steps**
1. Open basket/checkout form.
2. Click Confirm Order without filling fields.
3. Verify order not completed and page remains on basket.

**Expected result:** Empty checkout submission does not complete an order.  
**Actual result:** Page remained on basket.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-027 — TC-CHK-002: Verify missing billing email is invalid
**Test case ID:** TC-CHK-002  
**Test type:** Negative / Required  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Billing email empty  

**Test steps**
1. Open checkout form.
2. Clear billing email.
3. Evaluate native input validity.

**Expected result:** checkValidity() is false.  
**Actual result:** Native validity returned false.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-028 — TC-CHK-003: Verify punctuation-only postcode rejected
**Test case ID:** TC-CHK-003  
**Test type:** Boundary / Validation  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Postcode: !  

**Test steps**
1. Open basket checkout form.
2. Fill postcode with !.
3. Evaluate native HTML validity.

**Expected result:** checkValidity() is false.  
**Actual result:** Native validity returned true for !.  
**Execution status:** **FAIL**  
**Related defect:** BUG-CHK-001

### TCD-029 — TC-CHK-004: Verify invalid postcode rejected — symbol
**Test case ID:** TC-CHK-004  
**Test type:** Negative / Data-driven  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Postcode: !  

**Test steps**
1. Open checkout form.
2. Fill postcode with the provided dataset.
3. Evaluate native HTML checkValidity().

**Expected result:** checkValidity() is false for this malformed UK postcode.  
**Actual result:** Native validity accepted the test value.  
**Execution status:** **FAIL**  
**Related defect:** BUG-CHK-001

### TCD-030 — TC-CHK-004: Verify invalid postcode rejected — numbers
**Test case ID:** TC-CHK-004  
**Test type:** Negative / Data-driven  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Postcode: 123  

**Test steps**
1. Open checkout form.
2. Fill postcode with the provided dataset.
3. Evaluate native HTML checkValidity().

**Expected result:** checkValidity() is false for this malformed UK postcode.  
**Actual result:** Native validity accepted the test value.  
**Execution status:** **FAIL**  
**Related defect:** BUG-CHK-001

### TCD-031 — TC-CHK-004: Verify invalid postcode rejected — letters
**Test case ID:** TC-CHK-004  
**Test type:** Negative / Data-driven  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Postcode: ABCDE  

**Test steps**
1. Open checkout form.
2. Fill postcode with the provided dataset.
3. Evaluate native HTML checkValidity().

**Expected result:** checkValidity() is false for this malformed UK postcode.  
**Actual result:** Native validity accepted the test value.  
**Execution status:** **FAIL**  
**Related defect:** BUG-CHK-001

### TCD-032 — TC-CHK-004: Verify invalid postcode rejected — special-character
**Test case ID:** TC-CHK-004  
**Test type:** Negative / Data-driven  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Postcode: SW1A@1AA  

**Test steps**
1. Open checkout form.
2. Fill postcode with the provided dataset.
3. Evaluate native HTML checkValidity().

**Expected result:** checkValidity() is false for this malformed UK postcode.  
**Actual result:** Native validity accepted the test value.  
**Execution status:** **FAIL**  
**Related defect:** BUG-CHK-001

### TCD-033 — TC-CHK-005: Verify invalid billing email — missing-at
**Test case ID:** TC-CHK-005  
**Test type:** Negative / Data-driven  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** email without @  

**Test steps**
1. Open checkout form.
2. Fill billing email with invalid dataset.
3. Evaluate native HTML checkValidity().

**Expected result:** checkValidity() is false.  
**Actual result:** Native email validity rejected input.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-034 — TC-CHK-005: Verify invalid billing email — missing-domain
**Test case ID:** TC-CHK-005  
**Test type:** Negative / Data-driven  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** email without domain  

**Test steps**
1. Open checkout form.
2. Fill billing email with invalid dataset.
3. Evaluate native HTML checkValidity().

**Expected result:** checkValidity() is false.  
**Actual result:** Native email validity rejected input.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-035 — TC-CHK-005: Verify invalid billing email — plain-text
**Test case ID:** TC-CHK-005  
**Test type:** Negative / Data-driven  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** plain-text email input  

**Test steps**
1. Open checkout form.
2. Fill billing email with invalid dataset.
3. Evaluate native HTML checkValidity().

**Expected result:** checkValidity() is false.  
**Actual result:** Native email validity rejected input.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-036 — TC-CHK-006: Verify empty first name rejected
**Test case ID:** TC-CHK-006  
**Test type:** Negative / Required  
**Source:** `tests/test_checkout.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** First name empty  

**Test steps**
1. Open checkout form.
2. Locate first of the two input#name fields.
3. Clear its value.
4. Evaluate native checkValidity().

**Expected result:** First name is required; native validity is false.  
**Actual result:** Assertion passed after selector correction.  
**Execution status:** **PASS**  
**Related defect:** —

## Accessibility — 3 test executions

### TCD-037 — TC-A11Y-001: Verify unique HTML IDs — login page
**Test case ID:** TC-A11Y-001  
**Test type:** Accessibility / Structure  
**Source:** `tests/test_accessibility.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Page: /login  

**Test steps**
1. Open login page.
2. Collect nonempty DOM IDs.
3. Compare IDs for duplicates.

**Expected result:** No duplicated nonempty ID attributes.  
**Actual result:** No duplicate IDs detected.  
**Execution status:** **PASS**  
**Related defect:** —

### TCD-038 — TC-A11Y-001: Verify unique HTML IDs — basket page
**Test case ID:** TC-A11Y-001  
**Test type:** Accessibility / Structure  
**Source:** `tests/test_accessibility.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Page: /basket  

**Test steps**
1. Open basket page.
2. Collect nonempty DOM IDs.
3. Compare IDs for duplicates.

**Expected result:** No duplicated nonempty ID attributes.  
**Actual result:** ID name appeared twice on checkout form.  
**Execution status:** **FAIL**  
**Related defect:** BUG-A11Y-001

### TCD-039 — TC-A11Y-002: Verify login input accessible names
**Test case ID:** TC-A11Y-002  
**Test type:** Accessibility / Labels  
**Source:** `tests/test_accessibility.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Login email and password  

**Test steps**
1. Open login page.
2. Locate email and password by accessible names.

**Expected result:** Both controls expose usable accessible names.  
**Actual result:** Both matched expected accessible names.  
**Execution status:** **PASS**  
**Related defect:** —

## Images — 1 test executions

### TCD-040 — TC-IMG-001: Verify Wham Bars image loads
**Test case ID:** TC-IMG-001  
**Test type:** Functional / Image  
**Source:** `tests/test_images.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable.  
**Test data:** Product image alt: wham bar  

**Test steps**
1. Navigate to relevant product image.
2. Locate image.
3. Inspect load status / naturalWidth.

**Expected result:** Image has loaded with nonzero natural width.  
**Actual result:** Image failed to load; src ends in /img/whan.jpg.  
**Execution status:** **FAIL**  
**Related defect:** BUG-IMG-001

## Guest Basket — 1 test executions

### TCD-041 — Guest basket smoke test: Verify guest adds Chocolate Cups
**Test case ID:** Guest basket smoke test  
**Test type:** Positive / Smoke  
**Source:** `tests/test_helpers.py`  
**Preconditions:** A fresh isolated Chromium browser context; Sweet Shop is reachable. User is not logged in.  
**Test data:** Chocolate Cups  

**Test steps**
1. Open product catalog as guest.
2. Add Chocolate Cups to basket.
3. Open basket.
4. Verify item appears.

**Expected result:** Chocolate Cups displayed in guest basket.  
**Actual result:** Test passed.  
**Execution status:** **PASS**  
**Related defect:** —

## Defect traceability

| Finding | Test cases | Observed issue |
|---|---|---|
| BUG-A11Y-001 | TC-A11Y-001 [basket] | Duplicate `id="name"` in basket checkout form |
| BUG-BAS-001 | TC-BAS-005 | Shipping total is invalid / `£NaN` |
| BUG-CHK-001 | TC-CHK-003; TC-CHK-004 (four datasets) | Malformed UK postcodes pass native HTML validity |
| BUG-IMG-001 | TC-IMG-001 | Wham Bar image URL fails to load |
| BUG-LOG-001 | TC-LOG-005 | Wrong password led to demo account page |

**Evidence:** See `docs/bug_reports/` and selected screenshot copies in `docs/evidence/screenshots/` once they are added to the repository. Failed test execution alone is not proof of a security vulnerability; severity ratings require impact validation.

## Execution record

| Test run | Collected/executed | Passed | Failed | Duration |
|---|---:|---:|---:|---|
| Latest complete suite | 41 | 32 | 9 | 193.69 seconds |

