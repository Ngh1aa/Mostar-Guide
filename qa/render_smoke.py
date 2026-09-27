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


def assert_images_loaded(page, selector: str, label: str) -> None:
    broken = page.locator(selector).evaluate_all(
        "els => els.filter(el => !el.complete || el.naturalWidth === 0).map(el => el.getAttribute('src'))"
    )
    if broken:
        raise AssertionError(f"{label} contains broken images: {broken}")


def run_home(browser) -> None:
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    page_errors: list[str] = []
    failed_requests: list[str] = []
    page.on("pageerror", lambda exc: page_errors.append(str(exc)))
    page.on("requestfailed", lambda req: failed_requests.append(req.url))

    page.goto(f"{BASE_URL}/index.html", wait_until="networkidle")

    assert page.title() == "HUẾ — Between River & Citadel"
    assert page.locator("#cinema").count() == 1
    assert page.locator("#citadel").count() == 1
    assert page.locator("#river").count() == 1
    assert page.locator(".sight-card").count() == 15, "infinite slider must clone 3 sets of 5 cards"
    assert page.locator('a[href="routes.html"]').count() >= 1
    assert page.locator('img[src^="assets/hue/"]').count() >= 10
    assert_images_loaded(page, 'img[src^="assets/hue/"]', "Homepage Huế media")

    body_text = page.locator("body").inner_text()
    for stale in (
        "Mostar",
        "Bosnia and Herzegovina",
        "Stari Most",
        "Neretva",
        "Kujundžiluk",
        "Kujundziluk",
        "Koski Mehmed",
        "Kajtaz House",
        "War Photo Exhibition",
    ):
        assert stale not in body_text, f"stale destination identity visible on homepage: {stale}"

    checkpoints = [
        (0, "intro"),
        (900, "citadel"),
        (2140, "river"),
        (3560, "places"),
    ]
    for y, name in checkpoints:
        page.evaluate("y => window.scrollTo(0, y)", y)
        page.wait_for_timeout(900)
        page.screenshot(path=str(ARTIFACTS / f"home-{name}.png"), full_page=False)

        if name == "citadel":
            opacity = float(page.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--panel2-opacity') || 0"))
            assert_close(opacity, 0.8, "citadel panel opacity")
        elif name == "river":
            opacity = float(page.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--panel3-opacity') || 0"))
            assert_close(opacity, 0.8, "river panel opacity")
        elif name == "places":
            visibility = page.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--sights-visibility').trim()")
            assert visibility == "visible", f"places slider should be visible, got {visibility!r}"

    # Controls intentionally finish their own entrance later than the slider cards.
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
    failed_requests: list[str] = []
    page.on("pageerror", lambda exc: page_errors.append(str(exc)))
    page.on("requestfailed", lambda req: failed_requests.append(req.url))

    page.goto(f"{BASE_URL}/routes.html", wait_until="networkidle")

    assert page.title() == "Suggested routes — HUẾ · Between River & Citadel"
    assert page.locator("main#routes").count() == 1
    assert page.locator("article.route-card").count() == 3
    stop_counts = page.locator("article.route-card").evaluate_all(
        "cards => cards.map(card => card.querySelectorAll('ol.route-stops > li').length)"
    )
    assert stop_counts == [4, 5, 3], f"route stop counts changed: {stop_counts}"
    assert_images_loaded(page, 'img[src^="assets/hue/"]', "Routes Huế media")

    body_text = page.locator("body").inner_text()
    for stale in ("Mostar", "Stari Most", "Neretva", "Kujundžiluk", "Kujundziluk"):
        assert stale not in body_text, f"stale destination identity visible on routes: {stale}"

    scripts = page.locator("script[src]").evaluate_all("els => els.map(el => el.getAttribute('src'))")
    assert "routes.js" in scripts
    assert "script.js" not in scripts, "routes page must remain isolated from cinematic engine"

    page.screenshot(path=str(ARTIFACTS / "routes-desktop.png"), full_page=True)

    if page_errors:
        raise AssertionError(f"Routes JS errors: {page_errors}")
    local_failures = [url for url in failed_requests if url.startswith(BASE_URL)]
    if local_failures:
        raise AssertionError(f"Routes local request failures: {local_failures}")
    page.close()


def run_mobile(browser) -> None:
    for route in ("index.html", "routes.html"):
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.goto(f"{BASE_URL}/{route}", wait_until="networkidle")
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
