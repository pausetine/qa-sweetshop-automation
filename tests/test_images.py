
from tests.helpers import shop_page


def test_TC_IMG_001_wham_bars_image_loads(page):
    shop_page(page)

    image = page.locator(
        'img[alt="wham bar"]'
    )

    assert image.count() == 1, (
        "Expected exactly one Wham Bar image"
    )

    image.scroll_into_view_if_needed()

    result = image.evaluate(
        """img => ({
            src: img.src,
            loaded: img.complete && img.naturalWidth > 0
        })"""
    )

    assert result["loaded"], (
        f"Wham Bar image failed to load: {result['src']}"
    )
