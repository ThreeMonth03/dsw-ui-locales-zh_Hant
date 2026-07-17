# DSW UI Traditional Chinese Translations

This repository fills Traditional Chinese gaps in the official DSW UI locale. It stays synchronized
with the official Weblate catalogs while keeping confirmed local UI translations easy to edit.

## Start translating

1. Choose the branch matching your DSW version, such as `sync/v4.32`.
2. Open `translations/README.md` on that branch.
3. Choose an English source string and edit its `Translation (zh_Hant)` block in GitHub.
4. Open a pull request to the same version branch.

Each translation is a Markdown form. You do not need to edit PO files, write code, install tools, or
run a local Weblate server. CI validates the form, builds the locale, and provides a real DSW preview.

If the English text has no form, use an
[issue template](https://github.com/ThreeMonth03/dsw-ui-locales-zh_Hant/issues/new/choose) with the
DSW version, screen location, exact source text, and a screenshot.

Read the [contributor guide](CONTRIBUTING.md) or the
[translation website](https://www.threemonth03.com/dsw-ui-locales-zh_Hant/) for the complete workflow.

## Version branches

One `sync/vX.Y` branch is maintained for each supported DSW minor release. Versions 4.29 through
4.32 remain open for translation and are not archived. New official Weblate release lines are added
automatically when their source catalogs become available.

`main` contains shared policy and documentation. Translation forms live only on version branches.
