// Shared behaviour: mobile menu and copy-to-clipboard buttons.
(() => {
  "use strict";
  const btn = document.querySelector(".nav-btn");
  if (btn) {
    btn.addEventListener("click", () => {
      const open = btn.closest(".site-header").classList.toggle("nav-open");
      btn.setAttribute("aria-expanded", String(open));
    });
  }
  document.querySelectorAll("[data-copy]").forEach((b) => {
    b.addEventListener("click", async () => {
      const text = document.querySelector(b.dataset.copy)?.textContent.trim() || "";
      try {
        await navigator.clipboard.writeText(text);
        b.textContent = "Copied";
      } catch {
        b.textContent = "Select and copy";
      }
      setTimeout(() => (b.textContent = "Copy"), 2000);
    });
  });
})();
