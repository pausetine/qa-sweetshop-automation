# Test Case Matrix

**Status:** Designed / not executed against the live application. Test case IDs in this
matrix map directly to function names in `tests/`. Parametrized entries count as
multiple collected tests. Actual execution outcomes belong in the run report.

| Case ID | Scenario | Type | Expected behavior | Source |
|---|---|---|---|---|
| TC-NAV-001 | Homepage displays title | Positive | Welcome heading is visible | `test_navigation.py` |
| TC-NAV-002 | Browse Sweets link navigates | Positive | Catalog route and heading display | `test_navigation.py` |
| TC-NAV-003 | About page describes project | Positive | About heading and description display | `test_navigation.py` |
| TC-NAV-004 | Basket route accessible | Positive | Basket heading displays | `test_navigation.py` |
| TC-CAT-001 | Popular and boundary products present | Positive | Four expected product names display | `test_catalog.py` |
| TC-CAT-002 | Item pricing (3 datasets) | Positive | Price matches visible shop listing | `test_catalog.py` |
| TC-CAT-003 | Every product offers add action | Positive | 16 add controls are shown | `test_catalog.py` |
| TC-CAT-004 | Minimum listed price | Boundary | Bubbly costs £0.10 | `test_catalog.py` |
| TC-CAT-005 | Maximum listed price | Boundary | Swansea Mixture costs £1.50 | `test_catalog.py` |
| TC-BAS-001 | Empty cart value | Boundary | Shows £0.00 | `test_basket.py` |
| TC-BAS-002 | Add one product | Positive | Name and price appear in basket | `test_basket.py` |
| TC-BAS-003 | Sum two products | Positive | £0.95 + £0.75 = £1.70 | `test_basket.py` |
| TC-BAS-004 | Free collection | Boundary | Total remains £0.95 and numeric | `test_basket.py` |
| TC-BAS-005 | Standard shipping | Positive | £0.95 + £1.99 = £2.94, not NaN | `test_basket.py` |
| TC-BAS-006 | Redeem blank promo | Negative | Validation message shown | `test_basket.py` |
| TC-LOG-001 | Login with 3 published demo accounts | Positive | Redirect away from login | `test_login.py` |
| TC-LOG-002 | Missing email | Negative | Submission blocked | `test_login.py` |
| TC-LOG-003 | Invalid email (2 datasets) | Negative | Fails email validity | `test_login.py` |
| TC-LOG-004 | Missing password | Negative | Submission blocked | `test_login.py` |
| TC-LOG-005 | Wrong password | Negative | Login rejected | `test_login.py` |
| TC-CHK-001 | Submit entirely empty checkout | Negative | Cannot finish order | `test_checkout.py` |
| TC-CHK-002 | Empty billing email | Negative | Email validity rejects | `test_checkout.py` |
| TC-CHK-003 | One-character punctuation postcode | Boundary | Postcode must be rejected | `test_checkout.py` |
| TC-A11Y-001 | Duplicate HTML IDs (2 pages) | Accessibility | No duplicate IDs | `test_accessibility.py` |
| TC-A11Y-002 | Login accessible names | Accessibility | Email and password labels work | `test_accessibility.py` |

**31 tests collected** (`pytest --collect-only -q`).

## How to record test runs

| Run date | Browser | Pass | Fail | Error/Blocked | Evidence |
|---|---|---:|---:|---:|---|
| Not run yet | — | — | — | — | No live execution results available |

Separate **test failure** from **confirmed product bug**. A failed assertion could
be caused by changed labels/selectors, a test assumption, page timing, or a real defect.
Verify manually before filing a product bug. Before proposing a severity or priority,
consider business impact and repeatability. No full-payment submission is tested.
