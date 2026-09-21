# Translator guide

## Fill an empty translation

Choose the DSW version branch and open `translations/README.md`.
Use the pencil icon on a form and edit only its `Translation (zh_Hant)` block.
Leave the English source, hidden metadata, headings, and fences unchanged.

Keep placeholders and links intact. Read the interface context before choosing terminology.
Existing Traditional Chinese translations are the baseline; use the glossary where existing
usage does not provide an answer.

For metrics, use「權重」for `Weight` and「衡量值」for `Measure`.
FAIR metric names and descriptions belong to the Knowledge Model locale.

## Submit and review

Open a PR to the same `sync/vX.Y` branch. CI validates the contribution as data.
You do not need to regenerate the index or change version numbers.

Maintainers prepare a bounded Weblate submission and inspect its report before applying it.
New submissions are fuzzy, not approved. Nonempty official translations are protected by default.
A completed local form disappears after synchronization sees the same official translation;
the official fuzzy or approved state remains unchanged.

For a reported issue in existing wording, open a focused correction PR and link the discussion.
Existing translations are maintained, not archived. Do not rewrite unrelated wording.

## Maintainer actions

Run **Synchronize official translations** to refresh snapshots and forms.
Run **Submit translations to Weblate** with `apply` off to download a report and delta PO files.
After reviewing the report, use its plan hash as `expected_plan` and enable `apply`.
A changed batch is rejected, including changes to the proposed wording or prior Weblate values.

Uploads require the repository Actions secret `LOCALIZE_API_TOKEN`.
See the [maintainer guide](https://www.threemonth03.com/dsw-locale-tool/maintainers.html)
for permissions, conflicts, and verification.

GitHub Pages contains documentation only. This workflow does not deploy a DSW website.
