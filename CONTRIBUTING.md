# Contributing translations

You can contribute with GitHub's web editor. No programming or gettext knowledge is required.

## Edit a translation form

1. Select the `sync/vX.Y` branch for the DSW version you are translating.
2. Open `translations/README.md` and select a source string from the **Open** section.
3. Use the pencil icon to edit the file.
4. Fill only an empty `Translation (zh_Hant)` block, keeping its fences.
5. Propose the change as a pull request to the same `sync/vX.Y` branch.

Do not edit the English source, headings, hidden metadata, or fence markers. Preserve placeholders
such as `%s`, `{name}`, and `${value}` exactly. Follow `glossary/zh-Hant.csv` when it defines a term.

Only fields blank in the pull request's base may be changed. Reviewers may
revise new translations in that same PR, but must not rewrite existing text.
Nonempty official PO translations are protected too, including fuzzy entries
whose Markdown forms appear blank. Do not clear review flags. Report suspected
errors in existing translations separately for a maintainer's decision.

CI enforces this rule before merge and during cross-version propagation.
Official Weblate synchronization continues independently of this contributor policy.

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

Questionnaire questions and choices belong to the Knowledge Model locale. Exported document text
belongs to the Document Template. This repository covers DSW interface controls, navigation, and
system messages.

## License

By contributing translation content, you agree to publish it under the repository's CC BY 4.0
license.
