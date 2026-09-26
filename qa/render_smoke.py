from __future__ import annotations

import os
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE_URL = os.environ.get("QA_BASE_URL", "http://127.0.0.1:4173")
ARTIFACTS = Path("qa-artifacts")
ARTIFACTS.mkdir(exist_ok=True)


def assert_close(value: float, minimum: float, label: str) -> None:
    if value < minimum:
        raise AssertionError(f"{label}: expected >= {minimum}, got {value}")


def run_home(browser) -> None:
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    page_errors: list[str] = []
    failed_requests: list[str] = []
    page.on("pageerror", lambda exc: page_errors.append(str(exc)))
    page.on("requestfailed", lambda req: failed_requests.append(req.url))

    page.goto(f"{BASE_URL}/index.html", wait_until="domcontentloaded")
    page.wait_for_timeout(900)

    assert page.title() == "Mostar city"
    assert page.locator("#cinema").count() == 1
    assert page.locator("#bridge").count() == 1
    assert page.locator("#bazaar").count() == 1
    assert page.locator(".sight-card").count() == 15, "infinite slider must clone 3 sets of 5 cards"
    assert page.locator('a[href="routes.html"]').count() == 1

    checkpoints = [
        (0, "intro"),
        (900, "bridge"),
        (2140, "bazaar"),
        (3560, "sights"),
    ]
    for y, name in checkpoints:
        page.evaluate("y => window.scrollTo(0, y)", y)
        page.wait_for_timeout(900)
        page.screenshot(path=str(ARTIFACTS / f"home-{name}.png"), full_page=False)

        if name == "bridge":
            opacity = float(page.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--panel2-opacity') || 0"))
            assert_close(opacity, 0.8, "bridge panel opacity")
        elif name == "bazaar":
            opacity = float(page.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--panel3-opacity') || 0"))
            assert_close(opacity, 0.8, "bazaar panel opacity")
        elif name == "sights":
            visibility = page.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--sights-visibility').trim()")
            assert visibility == "visible", f"sights slider should be visible, got {visibility!r}"

    # Controls intentionally finish their own entrance later than the slider cards.
    # The immutable core only adds `.is-ready` after sightsControlsEnter > 0.98,
    # which occurs at the end of the 3360–3660 segment. Test the click there.
    page.evaluate("window.scrollTo(0, 3680)")
    page.wait_for_timeout(900)
    assert page.locator(".sights-controls.is-ready").count() == 1, "slider controls should be interactive after 3660px"

    before = page.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--sights-shift').trim()")
    page.locator(".sight-next").click()
    page.wait_for_timeout(120)
    after = page.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--sights-shift').trim()")
    assert before != after, "slider next control must change --sights-shift"

    if page_errors:
        raise AssertionError(f"Homepage JS errors: {page_errors}")

    local_failures = [url for url in failed_requests if url.startswith(BASE_URL)]
    if local_failures:
        raise AssertionError(f"Homepage local request failures: {local_failures}")

    page.close()


def run_routes(browser) -> None:
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    page_errors: list[str] = []
    page.on("pageerror", lambda exc: page_errors.append(str(exc)))

    page.goto(f"{BASE_URL}/routes.html", wait_until="domcontentloaded")
    page.wait_for_timeout(500)

    assert page.locator("main#routes").count() == 1
    assert page.locator("article.route-card").count() == 3
    stop_counts = page.locator("article.route-card").evaluate_all(
        "cards => cards.map(card => card.querySelectorAll('ol.route-stops > li').length)"
    )
    assert stop_counts == [4, 5, 3], f"route stop counts changed: {stop_counts}"

    scripts = page.locator("script[src]").evaluate_all("els => els.map(el => el.getAttribute('src'))")
    assert "routes.js" in scripts
    assert "script.js" not in scripts, "routes page must remain isolated from cinematic engine"

    page.screenshot(path=str(ARTIFACTS / "routes-desktop.png"), full_page=True)

    if page_errors:
        raise AssertionError(f"Routes JS errors: {page_errors}")
    page.close()


def run_mobile(browser) -> None:
    for route in ("index.html", "routes.html"):
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.goto(f"{BASE_URL}/{route}", wait_until="domcontentloaded")
        page.wait_for_timeout(500)
        overflow = page.evaluate("document.documentElement.scrollWidth - window.innerWidth")
        assert overflow <= 2, f"{route} horizontal overflow: {overflow}px"
        page.screenshot(path=str(ARTIFACTS / f"mobile-{route.replace('.html', '')}.png"), full_page=False)
        page.close()


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            run_home(browser)
            run_routes(browser)
            run_mobile(browser)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
