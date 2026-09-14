# Contributing translations

You can contribute with GitHub's web editor. No programming or gettext knowledge is required.

## Edit a translation form

1. Select the `sync/vX.Y` branch for the DSW version you are translating.
2. Open `translations/README.md`. Choose a blank form under **Open**, or find the
   form for a reported issue under **Open** or **Completed**.
3. Use the pencil icon to edit the file.
4. Edit only the `Translation (zh_Hant)` block, keeping its fences.
5. Propose the change as a pull request to the same `sync/vX.Y` branch.

Do not edit the English source, headings, hidden metadata, or fence markers. Preserve placeholders
such as `%s`, `{name}`, and `${value}` exactly. Follow `glossary/zh-Hant.csv` when it defines a term.

Prioritize empty fields and review the newly added translations. Leave existing
wording alone unless a problem has been identified; it is maintained, not frozen.
For a reported issue, propose a focused correction, link the report or discussion,
and explain the change. Nonempty fuzzy translations can also receive reviewed
corrections. Avoid unrelated rewrites and do not edit generated PO files or flags.

CI validates new translations and corrections alike. Automatic cross-version
propagation still fills only matching blanks; correct existing wording through
PRs to the affected branches. Official Weblate synchronization continues
independently.

CI checks the file structure and placeholders, builds the locale, and renders non-draft pull
requests in a disposable DSW installation. A pull-request comment links to the screenshots and
visible English-text report. An error message will identify any form that needs correction.
Generated indexes and immutable locale release versions are updated automatically after merge.

When you need to navigate the translated interface in a browser, ask a maintainer to add the
`live-preview` label. Contributors with label permission may add it directly. CI will add a
temporary read-only DSW link to the pull request; no local setup is required.

## Report a missing form or incorrect translation

Open an [issue](https://github.com/ThreeMonth03/dsw-ui-locales-zh_Hant/issues/new/choose) and provide:

1. The DSW version.
2. The page or navigation path.
3. The complete English source, including punctuation and placeholders.
4. A screenshot and reproduction steps.
5. A suggested Traditional Chinese translation, if available.

If an official translation needs correction but has no form, a maintainer can
prepare a form from its official POT entry for the same review workflow.

Questionnaire questions and choices belong to the Knowledge Model locale. Exported document text
belongs to the Document Template. This repository covers DSW interface controls, navigation, and
system messages.

## License

By contributing translation content, you agree to publish it under the repository's CC BY 4.0
license.
