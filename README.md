# Sweet Shop Web App Testing

**QA Automation Portfolio Project | Python · Playwright · Pytest**

**Application Under Test:** https://sweetshop.vivrichards.co.uk/about

Sweet Shop is an intentionally broken demonstration e-commerce application created by Viv Richards for software testing and Chrome DevTools practice.

This project is an independently developed **UI automation and defect-reporting portfolio**. It tests selected application features, validates expected behavior, and documents reproducible defects. It does not contain the source code of the Sweet Shop application.

## Project Snapshot

| Metric | Result |
|---|---|
| Automated test executions | **41** |
| Passed | **32** |
| Failed | **9** |
| Pass rate | **78.0%** |
| Documented QA findings | **5** |
| Testing techniques | Positive, negative, boundary, accessibility |
| Automation framework | Python, Playwright, Pytest |
| Execution date | October 27, 2026 |
| Evidence | Pytest execution report and failure screenshots |

**Note:** The nine failed tests correspond to five documented findings. The application is intentionally buggy, so failed assertions are retained as evidence rather than modified merely to achieve a passing test suite.


## Project Structure

```text
sweet-shop/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── helpers.py
│   ├── test_accessibility.py
│   ├── test_basket.py
│   ├── test_catalog.py
│   ├── test_checkout.py
│   ├── test_helpers.py
│   ├── test_images.py
│   ├── test_login.py
│   └── test_navigation.py
├── docs/
│   ├── test_cases.md
│   └── bug_reports/
│       ├── BUG_REPORT_TEMPLATE.md
│       ├── BUG-A11Y-001.md
│       ├── BUG-BAS-001.md
│       ├── BUG-CHK-001.md
│       ├── BUG-IMG-001.md
│       └── BUG-LOG-001.md
├── artifacts/
│   └── screenshots/
├── .github/
│   └── workflows/
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

The folder structure above is the recommended publishing layout. Verify that the actual files have been saved at these paths before committing.

## Test Coverage

### Navigation Testing
- Homepage rendering
- Browse Sweets navigation
- About page content
- Basket page navigation

### Product Catalog Testing
- Product presence and displayed names
- Product pricing
- Add to Basket controls
- Minimum and maximum listed prices

### Basket Testing
- Empty basket state
- Adding individual products
- Multiple-product subtotal calculation
- Free collection
- Standard shipping calculation
- Empty promotion-code validation

### Login Testing
- Three documented demo accounts
- Missing email
- Invalid email formats
- Missing password
- Incorrect password

### Checkout and Input Validation
- Empty checkout submission
- Required billing email
- Invalid UK postcode formats
- Empty first-name validation
- Additional email-format validation

No complete payment transactions were submitted.

### Accessibility Testing
- Duplicate HTML IDs
- Accessible names for login inputs

### Image Testing
- Product image loading
- Broken Wham Bars image detection

## Latest Complete Test Execution

**Date:** October 27, 2026  
**Environment:** Windows, Python 3.13.3, Chromium, Playwright 1.64.1, Pytest 9.1.1

| Test Module | Passed | Failed |
|---|---:|---:|
| Navigation | 3 | 1 |
| Catalog | 7 | 0 |
| Basket | 5 | 1 |
| Login | 7 | 1 |
| Checkout | 2 | 1 |
| Accessibility | 2 | 1 |
| Product Images | 0 | 1 |
| Guest Basket Smoke Test | 1 | 0 |
| **Total** | **27** | **6** |

The navigation failure involved a 10-second page-load timeout. TC-NAV-001 subsequently passed in isolation after changing the navigation wait to `domcontentloaded` and increasing the timeout.

The remaining five failures correspond to documented application findings.

## Documented Defects

| Bug ID | Description | Severity | Priority | Status |
|---|---|---|---|---|
| BUG-A11Y-001 | Duplicate HTML ID `name` on Basket page | Low | P2 | Reproduced |
| BUG-BAS-001 | Standard Shipping changes total to £NaN | High | P1 | Reproduced |
| BUG-CHK-001 | Invalid UK postcodes pass native HTML validation | Low | P2 | Validation gap reproduced |
| BUG-IMG-001 | Wham Bars product image fails to load | Low | P2 | Reproduced |
| BUG-LOG-001 | Incorrect password displays a demo account | High (provisional) | P1 | Reproduced |

**Total: 5 documented findings.**

The postcode issue is limited to demonstrated native HTML validation behavior; server-side acceptance has not been established.

The login finding was reproduced using a publicly documented demo account. Its impact on real customer accounts has not been established.

Each defect report includes reproduction steps, expected and actual results, severity, priority, linked test case, and supporting evidence.

## Additional Input-Validation Testing

Eight additional parameterized checks were executed separately:

| Validation | Cases | Results |
|---|---:|---|
| Invalid postcode formats | 4 | 4 failed |
| Invalid email formats | 3 | 3 passed |
| Empty first name | 1 | 1 passed |
| **Total** | **8** | **4 passed, 4 failed** |

The postcode tests used the following invalid values:

- `!`
- `123`
- `ABCDE`
- `SW1A@1AA`

These values passed native HTML constraint validation. All four results support BUG-CHK-001 rather than representing four separate bugs.

Input sanitization, server-side validation, and complete checkout behavior were not established by these tests.

## Getting Started

### Prerequisites

- Python 3.13 or another compatible Python version
- Git
- Chromium installed through Playwright
- Windows, macOS, or Linux

### Windows PowerShell

Open a terminal inside the project folder.

```powershell
py -m venv .venv

.\.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt

python -m playwright install chromium
```

If PowerShell blocks activation, run Python directly from the virtual environment:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

.\.venv\Scripts\python.exe -m playwright install chromium
```

### macOS / Linux

```bash
python3 -m venv .venv

source .venv/bin/activate

python -m pip install -r requirements.txt

python -m playwright install chromium
```

## Running Tests

### Run the complete suite

```powershell
python -m pytest tests/ -v
```

### Run specific test modules

```powershell
python -m pytest tests/test_catalog.py -v

python -m pytest tests/test_basket.py -v

python -m pytest tests/test_login.py -v

python -m pytest tests/test_checkout.py -v

python -m pytest tests/test_navigation.py -v

python -m pytest tests/test_accessibility.py -v

python -m pytest tests/test_images.py -v
```

### Run tests with a visible browser

```powershell
$env:HEADLESS="0"

python -m pytest tests/ -v -s
```

The project uses custom Playwright fixtures rather than relying on pytest-playwright's browser fixtures.

### Run selected test categories

```powershell
python -m pytest -m positive -v

python -m pytest -m negative -v

python -m pytest -m boundary -v

python -m pytest -m accessibility -v
```

### Run one specific test

```powershell
python -m pytest tests/test_basket.py::test_TC_BAS_005_standard_shipping_adds_1_99 -v -s
```

## Test Reports and Screenshots

To generate JUnit XML results:

```powershell
python -m pytest tests/ -v --junitxml=artifacts/junit.xml
```

For HTML reports, install `pytest-html` if it is not already included in `requirements.txt`:

```powershell
python -m pip install pytest-html
```

Then execute:

```powershell
python -m pytest tests/ -v --html=artifacts/report.html --self-contained-html
```

Screenshots of test failures are automatically saved in:

`artifacts/screenshots/`

These screenshots support defect investigation and demonstrate automated failure capture.

**Note:** The `artifacts/` directory is ignored by Git by default. Selected evidence must be explicitly included in the repository if public reviewers are expected to view it.

## Demo Login Accounts

Sweet Shop provides demonstration accounts for testing:

| Account | Email |
|---|---|
| One Order Customer | oneorder@sweetshop.local |
| Two Orders Customer | twoorders@sweetshop.local |
| Five Orders Customer | fiveorders@sweetshop.local |

**Published demo password:** `qwerty`

Only publicly provided demonstration credentials were used. No personal account credentials are required.

## QA Methodology

The project follows a structured testing process:

1. Identify a test scenario and expected result.
2. Inspect relevant HTML elements using Chrome DevTools.
3. Develop or refine Playwright selectors and assertions.
4. Execute tests using Pytest.
5. Investigate failed assertions and automation issues.
6. Reproduce suspected defects.
7. Document verified findings with screenshots and test references.
8. Retest after changes where applicable.

A failed automated test is not automatically considered a confirmed product defect. Selector errors, timing problems, incorrect assumptions, and environmental failures must be distinguished from application defects.

## Testing Limitations

- No real payment data or completed payment transactions were submitted.
- Successful guest checkout completion was not verified.
- Server-side validation and input sanitization were not comprehensively tested.
- Login testing used only public demonstration accounts.
- Accessibility checks were limited to specific HTML properties rather than a complete WCAG audit.
- Full cross-browser and mobile-device testing were not completed.
- Application behavior may change between test executions.
- The test suite does not represent exhaustive coverage of the Sweet Shop application.

## CI Workflow

A GitHub Actions workflow is included for executing tests and collecting artifacts.

It can be triggered manually through GitHub Actions, subject to the workflow configuration.

Because Sweet Shop is deliberately buggy, some assertions may fail as expected. All failures should be investigated and classified appropriately.

## Configuration Options

The project supports environment variables:

| Variable | Description |
|---|---|
| `BROWSER` | chromium, firefox, or webkit |
| `HEADLESS` | 0 to show browser; 1 to run headless |
| `BASE_URL` | Base URL of the application under test |

Example:

```powershell
$env:HEADLESS="0"
$env:BROWSER="chromium"

python -m pytest tests/ -v
```

Each test uses an isolated browser context.

## GitHub Publication

Create a repository, for example:

`github.com/pausetine/qa-sweetshop-automation`

From the project folder:

```bash
git init
git add .
git commit -m "Add verified Sweet Shop QA automation project"
git branch -M main
git remote add origin https://github.com/pausetine/qa-sweetshop-automation
git push -u origin main
```


## Resume / Portfolio Description

**Sweet Shop Web App Testing | Python, Playwright, Pytest**

- Developed and executed automated UI tests covering positive, negative, boundary, and accessibility scenarios against an intentionally buggy e-commerce application.
- Executed 41 automated checks in the latest complete suite run, with 32 passes and 9 failures.
- Documented five reproducible QA findings with test case references, severity, priority, reproduction steps, and screenshot evidence.
- Investigated failures using Chrome DevTools, Python assertions, DOM inspection, and Playwright browser automation.

## References

- [Sweet Shop — About](https://sweetshop.vivrichards.co.uk/about)
- [Sweet Shop — Login](https://sweetshop.vivrichards.co.uk/login)
- [Playwright Python Documentation](https://playwright.dev/python/docs/intro)
- [Pytest Documentation](https://docs.pytest.org/)
- [Site Creator — Shipping Defect Demonstration](https://vivrichards.co.uk/devtools/debugging-with-chrome-devtools-ai-assistance)
- [Site Creator — Duplicate HTML ID Discussion](https://vivrichards.co.uk/devtools/devtools-ai-assistance-find-selectors-a-handy-assistant-not-replacement)

---

**Project Status:** Test execution and initial defect documentation completed. Further test improvements, cross-browser verification, and defect retesting remain possible.