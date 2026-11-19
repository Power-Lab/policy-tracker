(() => {
  "use strict";

  // Where review issues are filed. On <owner>.github.io/<repo>/ this is worked out from the URL.
  const FALLBACK_REPO = document.body.dataset.repo || "Power-Lab/policy-tracker";  // set by the build
  const DRAFTS_KEY = "sea-tracker-review-drafts";
  const NAME_KEY = "sea-tracker-reviewer";
  const LIST = new Set(["energy_channel", "topics", "amends", "revokes"]);
  const DERIVED = new Set(["amended_by", "revoked_by", "implemented_by", "overridden_by", "slug", "categories"]);
  const CHECKS = [
    ["status", "Status matches the official text and any later rules"],
    ["links", "Each amends / revokes link confirmed in the text"],
    ["dates", "Signed and in-force dates confirmed"],
    ["summary", "English title and summary are accurate"],
    ["source", "Source URL points to the document itself"],
  ];
  // Fields shown in the editor, in order. Others are kept as they are.
  const FIELDS = [
    ["status", "select"], ["date_signed"], ["date_in_force"],
    ["amends", "ids"], ["revokes", "ids"], ["implements", "ids"], ["overrides", "ids"], ["link_basis", "select"],
    ["title_english"], ["summary_english", "textarea"], ["title_original"],
    ["number"], ["short_name"], ["issuing_body"], ["doc_type", "select"], ["origin_sector", "select"],
    ["energy_channel", "multi"], ["topics", "multi"], ["technologies", "multi"],
    ["binding", "select"], ["grandfathered"], ["jurisdiction"],
    ["source_url"], ["source_type", "select"], ["notes", "textarea"],
  ];

  let DATA, BY_ID, selected = null, MULTI = false, MAX = 10;
  const store = {
    get(k, d) { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* storage blocked */ } },
  };
  let drafts = store.get(DRAFTS_KEY, {}); // id -> {fields:{...}, checks:{...}}

  const $ = (s) => document.querySelector(s);
  const el = (tag, attrs = {}, ...kids) => {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (k === "class") n.className = v;
      else if (k === "text") n.textContent = v;
      else if (v === true) n.setAttribute(k, "");
      else if (v !== false && v != null) n.setAttribute(k, v);
    }
    for (const k of kids.flat()) if (k != null) n.append(k);
    return n;
  };
  const today = () => new Date().toISOString().slice(0, 10);
  const asText = (v) => (Array.isArray(v) ? v.join(";") : v ?? "");
  const repo = () => {
    const m = location.hostname.match(/^([^.]+)\.github\.io$/);
    const seg = location.pathname.split("/").filter(Boolean)[0];
    return m && seg && seg !== "review.html" ? `${m[1]}/${seg}` : FALLBACK_REPO;
  };

  const ROOT = document.body.dataset.root || "";
  fetch(`${ROOT}data/rules.json`).then((r) => r.json()).then((data) => {
    DATA = data;
    BY_ID = Object.fromEntries(data.rules.map((r) => [r.id, r]));
    const name = $("#reviewer");
    name.value = store.get(NAME_KEY, "");
    name.addEventListener("input", () => store.set(NAME_KEY, name.value.trim()));
    for (const [code, label] of Object.entries(data.countries)) {
      const i = el("input", { type: "checkbox", value: code });
      i.addEventListener("change", renderQueue);
      $("#f-country").append(el("label", { class: "check" }, i, ` ${label}`));
    }
    $("#q").addEventListener("input", renderQueue);
    $("#only-open").addEventListener("change", renderQueue);
    $("#dl").addEventListener("click", downloadCsv);
    MULTI = !!(data.config && data.config.reviews && data.config.reviews.multi_rule);
    MAX = (data.config && data.config.reviews && data.config.reviews.max_rules_per_review) || 10;
    const all = $("#submit-all");
    if (MULTI) {
      all.hidden = false;
      all.addEventListener("click", () => {
        const ids = Object.keys(drafts);
        if (ids.length > MAX) { alert(`Submit at most ${MAX} rules per review. Discard or submit some drafts first.`); return; }
        openIssue(ids);
      });
    }
    $("#discard-all").addEventListener("click", () => {
      if (!Object.keys(drafts).length || !confirm("Discard all drafts in this browser?")) return;
      drafts = {}; store.set(DRAFTS_KEY, drafts); renderQueue(); renderEditor();
    });
    const m = location.hash.match(/rule=([^&]+)/);
    if (m) selected = decodeURIComponent(m[1]);
    renderQueue(); renderEditor();
  });

  // The row as the reviewer currently sees it: published data plus their draft.
  const current = (id) => ({ ...BY_ID[id], ...(drafts[id]?.fields || {}) });

  function renderQueue() {
    const q = $("#q").value.trim().toLowerCase();
    const countries = [...document.querySelectorAll("#f-country input:checked")].map((i) => i.value);
    const onlyOpen = $("#only-open").checked;
    const rows = DATA.rules.filter((r) =>
      (!countries.length || countries.includes(r.country)) &&
      (!onlyOpen || r.verification !== "verified" || drafts[r.id]) &&
      (!q || [r.id, r.short_name, r.number, r.title_english].join(" ").toLowerCase().includes(q)));
    // Rules with amendment links first: they are where errors matter most.
    rows.sort((a, b) => (!!drafts[b.id] - !!drafts[a.id]) ||
      ((b.amends.length + b.revokes.length + b.amended_by.length + b.revoked_by.length) -
       (a.amends.length + a.revokes.length + a.amended_by.length + a.revoked_by.length)) ||
      a.id.localeCompare(b.id));
    const n = Object.keys(drafts).length;
    $("#count").textContent = `${rows.length} in queue · ${n} draft${n === 1 ? "" : "s"}`;
    $("#queue").replaceChildren(...rows.map((r) => el("li", {},
      el("a", { href: `#rule=${encodeURIComponent(r.id)}`, class: r.id === selected ? "selected" : "" },
        el("span", { class: "flag", text: r.country }), " ", r.short_name,
        drafts[r.id] ? el("span", { class: "draft-dot", title: "Has a draft", text: "●" }) : null,
        el("span", { class: "v", text: r.verification })))));
    $("#dl").disabled = !n;
    const all = $("#submit-all");
    if (all) { all.disabled = !n; all.textContent = `Submit ${n || ""} draft${n === 1 ? "" : "s"} as one review`.replace("  ", " "); }
  }

  window.addEventListener("hashchange", () => {
    const m = location.hash.match(/rule=([^&]+)/);
    selected = m ? decodeURIComponent(m[1]) : null;
    renderQueue(); renderEditor();
  });

  function setDraft(id, field, value) {
    const d = drafts[id] || (drafts[id] = { fields: {}, checks: {} });
    const orig = asText(BY_ID[id][field]);
    if (asText(value) === orig) delete d.fields[field]; else d.fields[field] = value;
    if (!Object.keys(d.fields).length && !Object.values(d.checks).some(Boolean)) delete drafts[id];
    store.set(DRAFTS_KEY, drafts);
  }
  function setCheck(id, key, on) {
    const d = drafts[id] || (drafts[id] = { fields: {}, checks: {} });
    d.checks[key] = on;
    if (!Object.keys(d.fields).length && !Object.values(d.checks).some(Boolean)) delete drafts[id];
    store.set(DRAFTS_KEY, drafts);
  }
  const verificationFor = (id) => {
    const c = drafts[id]?.checks || {};
    const n = CHECKS.filter(([k]) => c[k]).length;
    return n === CHECKS.length ? "verified" : n ? "partly verified" : BY_ID[id].verification;
  };

  // Mirrors the consistency checks in scripts/build.py, run against the draft.
  function problems(id) {
    const r = current(id), out = [];
    const ids = (v) => (Array.isArray(v) ? v : String(v).split(";").map((s) => s.trim()).filter(Boolean));
    for (const f of ["amends", "revokes", "implements", "overrides"]) for (const t of ids(r[f])) {
      if (!BY_ID[t]) out.push(`${f}: unknown id "${t}" (add that rule first, or fix the id)`);
      else if (f === "revokes" && !["draft", "pending"].includes(r.status) && !["revoked", "replaced", "expired"].includes(current(t).status))
        out.push(`This rule revokes ${BY_ID[t].short_name}, which is still marked "${current(t).status}". Update that row too.`);
      else if (f === "amends" && !["draft", "pending"].includes(r.status) && current(t).status === "in force")
        out.push(`This rule amends ${BY_ID[t].short_name}, which is marked "in force"; it should probably read "amended".`);
    }
    if (r.revoked_by.length && !["revoked", "replaced", "expired"].includes(r.status))
      out.push(`Revoked by ${r.revoked_by.map((x) => BY_ID[x].short_name).join(", ")} but status is "${r.status}".`);
    for (const f of ["date_signed", "date_in_force"])
      if (r[f] && !/^\d{4}(-\d{2}(-\d{2})?)?$/.test(r[f])) out.push(`${f} must be YYYY, YYYY-MM or YYYY-MM-DD.`);
    return out;
  }

  function renderEditor() {
    const box = $("#editor");
    if (!selected || !BY_ID[selected]) { box.replaceChildren(el("p", { class: "muted", text: "Pick a rule from the queue." })); return; }
    const id = selected, orig = BY_ID[id], r = current(id);
    const changed = (f) => drafts[id]?.fields && f in drafts[id].fields;

    const input = (f, kind) => {
      const opts = DATA.vocab[f] || (f === "topics" ? DATA.topics.map((t) => t.id) : []);
      let node;
      if (kind === "select") {
        node = el("select", {}, ...opts.map((o) => el("option", { value: o, text: o, selected: r[f] === o })));
      } else if (kind === "multi") {
        const vals = new Set(Array.isArray(r[f]) ? r[f] : String(r[f]).split(";"));
        node = el("div", { class: "multi" }, ...opts.map((o) => {
          const cb = el("input", { type: "checkbox", value: o, checked: vals.has(o) });
          cb.addEventListener("change", () => {
            const v = [...node.querySelectorAll("input:checked")].map((i) => i.value);
            setDraft(id, f, v); refresh();
          });
          return el("label", { class: "check" }, cb, ` ${o}`);
        }));
        return node;
      } else if (kind === "textarea") {
        node = el("textarea", { rows: f === "notes" ? 3 : 4 });
        node.value = asText(r[f]);
      } else {
        node = el("input", { type: "text", placeholder: kind === "ids" ? "ids separated by ;" : "" });
        node.value = asText(r[f]);
      }
      node.addEventListener("change", () => {
        const v = kind === "ids" ? node.value.split(";").map((s) => s.trim()).filter(Boolean) : node.value.trim();
        setDraft(id, f, v); refresh();
      });
      return node;
    };

    const refresh = () => { renderQueue(); renderEditor(); };
    const issues = problems(id);
    const checks = drafts[id]?.checks || {};

    box.replaceChildren(...[
      el("div", { class: "detail-head" },
        el("p", { class: "eyebrow", text: `${DATA.countries[orig.country]} · ${orig.doc_type} · ${id}` }),
        el("h2", { text: orig.short_name }),
        el("p", { class: "orig", lang: orig.language, text: orig.title_original }),
        el("p", {}, el("a", { href: orig.source_url, target: "_blank", rel: "noopener", text: "Open the official source ↗" }),
          " · ", el("a", { href: `${ROOT}rules/${orig.slug}/`, text: "Public page" }))),
      orig.notes ? el("div", { class: "callout warn small", text: orig.notes }) : null,
      el("h3", { text: "Checklist" }),
      el("div", { class: "checklist" }, ...CHECKS.map(([k, label]) => {
        const cb = el("input", { type: "checkbox", checked: !!checks[k] });
        cb.addEventListener("change", () => { setCheck(id, k, cb.checked); refresh(); });
        return el("label", { class: "check" }, cb, ` ${label}`);
      })),
      el("p", { class: "small" }, "Verification will be set to ", el("strong", { class: "verif-result", text: verificationFor(id) }), "."),
      issues.length ? el("ul", { class: "problems" }, ...issues.map((p) => el("li", { text: p }))) : null,
      el("h3", { text: "Fields" }),
      el("p", { class: "small muted" }, "Linked rules: ",
        ...["amended_by", "revoked_by"].flatMap((f) => orig[f].length
          ? [`${f.replace("_", " ")} `, ...orig[f].flatMap((x, i) => [i ? ", " : "", el("a", { href: `#rule=${encodeURIComponent(x)}`, text: BY_ID[x].short_name })]), ". "]
          : [])),
      el("div", { class: "form" }, ...FIELDS.map(([f, kind]) =>
        el("label", { class: "form-row" + (changed(f) ? " changed" : "") },
          el("span", { text: f + (changed(f) ? " (edited)" : "") }), input(f, kind),
          changed(f) ? el("span", { class: "was", text: `was: ${asText(orig[f]) || "—"}` }) : null))),
      el("div", { class: "actions" },
        el("button", { type: "button", class: "btn", id: "issue", disabled: !drafts[id] }, "Submit this rule as a GitHub issue"),
        el("button", { type: "button", class: "btn btn-ghost", id: "discard", disabled: !drafts[id] }, "Discard this draft")),
    ].filter(Boolean));
    box.querySelector("#issue").addEventListener("click", () => openIssue([id]));
    box.querySelector("#discard").addEventListener("click", () => { delete drafts[id]; store.set(DRAFTS_KEY, drafts); refresh(); });
  }

  function finalRow(id) {
    const r = { ...current(id) };
    const v = verificationFor(id);
    if (drafts[id] && Object.values(drafts[id].checks).some(Boolean)) {
      r.verification = v;
      r.reviewed_by = store.get(NAME_KEY, "") || "unnamed reviewer";
      r.reviewed_on = today();
      r.status_checked = drafts[id].checks.status ? today() : r.status_checked;
    }
    return r;
  }

  // Review issues carry a fenced ```json review block that the review-to-PR workflow reads.
  // Only edited fields are sent, each with the value the reviewer started from ("base"),
  // so the workflow can refuse to overwrite a field someone else changed in the meantime.
  // Verification, reviewer and dates are worked out by the workflow from the checklist.
  function payloadFor(ids) {
    return {
      v: 1,
      reviewer: store.get(NAME_KEY, ""),
      rules: ids.map((id) => {
        const d = drafts[id] || { fields: {}, checks: {} };
        const set = {}, base = {};
        for (const [f, val] of Object.entries(d.fields)) { set[f] = asText(val); base[f] = asText(BY_ID[id][f]); }
        return { id, base, set, checks: Object.fromEntries(CHECKS.map(([k]) => [k, !!d.checks[k]])) };
      }),
    };
  }

  function reviewBody(ids) {
    const lines = [`Review by ${store.get(NAME_KEY, "")} of ${ids.length} rule${ids.length === 1 ? "" : "s"}.`, ""];
    for (const id of ids) {
      const orig = BY_ID[id], d = drafts[id] || { fields: {}, checks: {} };
      lines.push(`### ${orig.short_name} (\`${id}\`)`, "");
      lines.push(...CHECKS.map(([k, l]) => `- [${d.checks[k] ? "x" : " "}] ${l}`), "");
      const fs = Object.keys(d.fields);
      if (fs.length) {
        lines.push("| field | was | now |", "| --- | --- | --- |");
        const cell = (v) => asText(v).replace(/\|/g, "\\|").replace(/\n/g, " ") || "—";
        for (const f of fs) lines.push(`| ${f} | ${cell(orig[f])} | ${cell(d.fields[f])} |`);
      } else lines.push("_No field changes; checklist only._");
      lines.push("");
    }
    lines.push("<details><summary>Machine-readable review (used by the workflow; please do not edit)</summary>", "",
      "```json review", JSON.stringify(payloadFor(ids)), "```", "", "</details>");
    return lines.join("\n");
  }

  async function openIssue(ids) {
    if (!store.get(NAME_KEY, "")) { alert("Add your name first."); $("#reviewer").focus(); return; }
    const title = ids.length === 1
      ? `Review: ${BY_ID[ids[0]].short_name} (${ids[0]})`
      : `Review: ${ids.length} rules (${[...new Set(ids.map((i) => BY_ID[i].country))].join(", ")})`;
    const body = reviewBody(ids);
    const base = `https://github.com/${repo()}/issues/new?`;
    let url = base + new URLSearchParams({ title, body, labels: "review" });
    // Browsers and GitHub cut off very long URLs; fall back to the clipboard.
    if (url.length > 7500) {
      try { await navigator.clipboard.writeText(body); } catch { /* handled below */ }
      alert("This review is too long to prefill. It has been copied to your clipboard: paste it into the issue body on the next page.");
      url = base + new URLSearchParams({ title, labels: "review", body: "(paste the review here)" });
    }
    window.open(url, "_blank", "noopener");
  }

  const csvCell = (v) => (/[",\n]/.test(v) ? `"${v.replace(/"/g, '""')}"` : v);
  const csvLine = (cells) => cells.map((c) => csvCell(String(c))).join(",");

  function downloadCsv() {
    const lines = [csvLine(DATA.columns)];
    // rules.json keeps the CSV's row order, so this diffs cleanly against data/rules.csv.
    for (const r of DATA.rules) {
      const row = drafts[r.id] ? finalRow(r.id) : r;
      lines.push(csvLine(DATA.columns.map((c) => asText(row[c]))));
    }
    const blob = new Blob([lines.join("\n") + "\n"], { type: "text/csv" });
    const a = el("a", { href: URL.createObjectURL(blob), download: "rules.csv" });
    document.body.append(a); a.click(); a.remove();
  }
})();
