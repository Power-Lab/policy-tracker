// Compare page: show or hide country columns and category rows; settings are kept in the URL.
(() => {
  "use strict";
  const form = document.getElementById("compare-controls");
  if (!form) return;
  const boxes = [...form.querySelectorAll('input[name="country"]')];
  const radios = [...form.querySelectorAll('input[name="category"]')];

  function apply(write) {
    const shown = new Set(boxes.filter((b) => b.checked).map((b) => b.value));
    const cat = (radios.find((r) => r.checked) || {}).value || "";
    document.querySelectorAll(".matrix [data-country]").forEach((el) => { el.hidden = !shown.has(el.dataset.country); });
    document.querySelectorAll(".matrix tr[data-category]").forEach((tr) => { tr.hidden = !!cat && tr.dataset.category !== cat; });
    document.querySelectorAll(".matrix .group-row th").forEach((th) => th.setAttribute("colspan", String(shown.size + 1)));
    if (write) {
      const p = new URLSearchParams();
      if (shown.size !== boxes.length) shown.forEach((c) => p.append("country", c));
      if (cat) p.set("category", cat);
      const q = p.toString();
      history.replaceState(null, "", q ? `?${q}` : location.pathname);
    }
  }

  const p = new URLSearchParams(location.search);
  const want = p.getAll("country");
  if (want.length) boxes.forEach((b) => (b.checked = want.includes(b.value)));
  const cat = p.get("category");
  if (cat) radios.forEach((r) => (r.checked = r.value === cat));
  form.addEventListener("change", () => apply(true));
  apply(false);
})();
