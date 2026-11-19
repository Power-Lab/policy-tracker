# How reviews work

Reviews turn `unverified` entries into `verified` ones. A reviewer checks an entry against the official text and submits it from the site; GitHub Actions turns the submission into a pull request; a maintainer merges it and the site updates.

```
Reviewer view ──► GitHub issue ──► "Review to pull request" workflow ──► pull request ──► maintainer merges ──► site rebuilds
 (/review/)       (review block)    applies edits, runs all checks         (summary +        (one click)          (~1 minute)
                                     comments on the issue                 warnings)
```

## For reviewers

1. Open the reviewer view (`/review/` on the tracker site, e.g. https://power-lab.github.io/policy-tracker/review/) and enter your name (for example "A. Reviewer (IESR)").
2. Pick an entry. Entries with amendment links come first, because that's where mistakes matter most.
3. Open the official source, then work through the checklist:
   - status matches the official text and any later rules
   - each amends / revokes link is confirmed in the text
   - signed and in-force dates are confirmed
   - the English title and summary are accurate
   - the source URL points to the document itself
4. Fix any field that is wrong. Edited fields are highlighted, with the old value shown underneath.
5. Submit:
   - **Submit this rule as a GitHub issue:** one rule.
   - **Submit drafts as one review:** every rule you have drafts for, in one issue (up to 10). Use this when rules belong together, for example a new rule plus the older rule it revokes.
6. GitHub opens with the issue filled in. Press **Submit new issue**. You need a (free) GitHub account.

Within a minute the workflow comments on your issue with a link to the pull request, or explains what went wrong. If you edit the issue, the pull request updates.

Ticking all five checks sets the entry to **verified**; ticking some sets **partly verified**. Your name, your GitHub username and the date are recorded on the entry. Ticking the status check also updates "status checked".

Drafts are kept in your browser until you submit or discard them. They never leave your computer otherwise.

## For maintainers

### What the workflow does

`.github/workflows/review-to-pr.yml` runs when an issue is opened or edited and either has the `review` label or contains a ```` ```json review ```` block. It:

1. adds the `review` label (creating the `review` and `correction` labels if they don't exist),
2. runs `scripts/apply_review.py`, which reads only the JSON block and
   - changes only the fields listed in `EDITABLE`; never `id`, `country` or the verification fields directly,
   - refuses to overwrite a field that changed since the reviewer loaded the page, and reports it as a conflict,
   - sets `verification`, `reviewed_by`, `reviewed_on` and `status_checked` from the checklist,
3. runs data validation, the unit tests, the site build and the link check,
4. pushes branch `review/issue-<n>` and opens (or updates) a pull request that says `Closes #<n>`,
5. comments on the issue with the result.

The pull request body lists every field change and any status warnings, for example "this now revokes Decree 80/2024, which is still marked in force". Merging publishes the change and closes the issue.

### Settings this needs (one time)

- **Settings → Actions → General → Workflow permissions:** allow *Read and write permissions* and tick **Allow GitHub Actions to create and approve pull requests**. Without this, the workflow can't open the pull request.

Note: GitHub doesn't run other workflows on pull requests opened by Actions. That's why the review workflow runs every check itself before opening the PR. The normal build runs again when the PR is merged to `main`.

### Settings in `config.json`

```json
{
  "reviews": {
    "multi_rule": true,
    "max_rules_per_review": 10
  }
}
```

- `multi_rule`: `false` hides the "submit drafts as one review" button, and the workflow rejects reviews that cover more than one rule.
- `max_rules_per_review`: upper limit when multi-rule reviews are on.

### Pull requests from people

Edits to `data/rules.csv` can also come as ordinary pull requests. The build workflow adds a "Changes to the data" table to the run summary, and must pass before merging.

### Security notes

- Issue text is untrusted. It reaches the script only through an environment variable, and only the JSON block is read. Nothing in it is executed.
- Anyone with a GitHub account can submit a review, so a person always merges. Don't enable auto-merge for review PRs unless you restrict it to a list of trusted reviewers.
