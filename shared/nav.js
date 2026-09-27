(() => {
  const stops = new Map([
    ["#cinema", 0],
    ["#citadel", 900],
    ["#river", 2140],
  ]);

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  function goToStoryStop(hash, updateHistory = true) {
    const offset = stops.get(hash);
    const cinema = document.querySelector("#cinema");
    if (offset == null || !cinema) return false;

    if (updateHistory && window.location.hash !== hash) {
      history.pushState(null, "", hash);
    }

    window.scrollTo({
      top: cinema.offsetTop + offset,
      behavior: reduceMotion.matches ? "auto" : "smooth",
    });
    return true;
  }

  document.addEventListener("click", (event) => {
    const link = event.target.closest('a[href^="#"]');
    if (!link || !stops.has(link.getAttribute("href"))) return;
    event.preventDefault();
    goToStoryStop(link.getAttribute("href"));
  });

  window.addEventListener("DOMContentLoaded", () => {
    if (!stops.has(window.location.hash)) return;
    requestAnimationFrame(() => goToStoryStop(window.location.hash, false));
  });

  window.addEventListener("popstate", () => {
    if (stops.has(window.location.hash)) goToStoryStop(window.location.hash, false);
  });
})();
