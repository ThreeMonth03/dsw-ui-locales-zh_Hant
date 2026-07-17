# Contributing translations

You can contribute with GitHub's web editor. No programming or gettext knowledge is required.

## Edit a translation form

1. Select the `sync/vX.Y` branch for the DSW version you are translating.
2. Open `translations/README.md` and select a source string.
3. Use the pencil icon to edit the file.
4. Enter Traditional Chinese only between the fences under `Translation (zh_Hant)`.
5. Propose the change as a pull request to the same `sync/vX.Y` branch.

Do not edit the English source, headings, hidden metadata, or fence markers. Preserve placeholders
such as `%s`, `{name}`, and `${value}` exactly. Follow `glossary/zh-Hant.csv` when it defines a term.

CI checks the file structure and placeholders, builds the locale, and packages a preview artifact.
An error message will identify the form that needs correction.

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
