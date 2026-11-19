// Explore page: filters, search and sort over the pre-rendered result list.
// State lives in the URL query (?q=…&country=ID&topic=rooftop-solar), so views can be shared.
(() => {
  "use strict";
  const KEYS = ["category", "country", "status", "topic", "technology", "doc_type", "verification"];
  const MULTI = new Set(["topic", "category", "technology"]);  // space-separated lists in data attributes
  const list = document.getElementById("results");
  const items = [...list.querySelectorAll(".result")];
  const q = document.getElementById("q");
  const sort = document.getElementById("sort");
  const boxes = [...document.querySelectorAll(".facets input[type=checkbox]")];
  const labelOf = (key, value) => {
    const box = boxes.find((b) => b.name === key && b.value === value);
    return box ? box.parentElement.querySelector("span").textContent.trim() : value;
  };

  const values = (el, key) => (MULTI.has(key) ? el.dataset[key].split(" ").filter(Boolean) : [el.dataset[key]]);

  function readUrl() {
    const p = new URLSearchParams(location.search);
    q.value = p.get("q") || "";
    sort.value = p.get("sort") || "new";
    for (const b of boxes) b.checked = p.getAll(b.name).includes(b.value);
  }

  function writeUrl() {
    const p = new URLSearchParams();
    if (q.value.trim()) p.set("q", q.value.trim());
    for (const b of boxes) if (b.checked) p.append(b.name, b.value);
    if (sort.value !== "new") p.set("sort", sort.value);
    const s = p.toString();
    history.replaceState(null, "", s ? `?${s}` : location.pathname);
  }

  function selected() {
    const sel = {};
    for (const k of KEYS) sel[k] = boxes.filter((b) => b.name === k && b.checked).map((b) => b.value);
    return sel;
  }

  function matches(el, sel, words, skip) {
    for (const k of KEYS) {
      if (k === skip || !sel[k].length) continue;
      if (!values(el, k).some((v) => sel[k].includes(v))) return false;
    }
    return words.every((w) => el.dataset.text.includes(w));
  }

  function apply() {
    const sel = selected();
    const words = q.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let shown = 0;
    for (const el of items) {
      const ok = matches(el, sel, words);
      el.hidden = !ok;
      shown += ok;
    }
    // Facet counts: how many results each option would give, keeping the other filters.
    for (const b of boxes) {
      const n = items.filter((el) => matches(el, sel, words, b.name) && values(el, b.name).includes(b.value)).length;
      const span = b.parentElement.querySelector(".n");
      if (span) span.textContent = n;
      b.parentElement.classList.toggle("zero", n === 0 && !b.checked);
    }
    const sorted = [...items].sort(compare(sort.value));
    list.append(...sorted);
    document.getElementById("result-count").textContent = `${shown} rule${shown === 1 ? "" : "s"}`;
    document.getElementById("no-results").hidden = shown > 0;
    renderChips(sel);
    writeUrl();
  }

  function compare(mode) {
    const d = (el) => el.dataset.date || "0000";
    return {
      new: (a, b) => d(b).localeCompare(d(a)),
      old: (a, b) => d(a).localeCompare(d(b)),
      country: (a, b) => a.dataset.country.localeCompare(b.dataset.country) || d(b).localeCompare(d(a)),
      name: (a, b) => a.dataset.name.localeCompare(b.dataset.name, undefined, { numeric: true }),
    }[mode] || (() => 0);
  }

  function renderChips(sel) {
    const box = document.getElementById("active-filters");
    box.replaceChildren();
    for (const k of KEYS) {
      for (const v of sel[k]) {
        const chip = document.createElement("button");
        chip.type = "button";
        chip.className = "chip-btn";
        chip.textContent = labelOf(k, v);
        chip.setAttribute("aria-label", `Remove filter ${labelOf(k, v)}`);
        chip.addEventListener("click", () => {
          boxes.find((b) => b.name === k && b.value === v).checked = false;
          apply();
        });
        box.append(chip);
      }
    }
  }

  function clear() {
    q.value = "";
    boxes.forEach((b) => (b.checked = false));
    apply();
  }

  readUrl();
  // Open any collapsed facet that has an active filter.
  document.querySelectorAll(".facet").forEach((f) => {
    if (f.querySelector("input:checked")) f.open = true;
  });
  boxes.forEach((b) => b.addEventListener("change", apply));
  q.addEventListener("input", apply);
  sort.addEventListener("change", apply);
  document.getElementById("clear").addEventListener("click", clear);
  document.getElementById("clear-2").addEventListener("click", clear);
  apply();
})();
