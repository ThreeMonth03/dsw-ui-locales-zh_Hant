# DSW UI Traditional Chinese Translations

This repository fills Traditional Chinese gaps in the official DSW UI locale. It stays synchronized
with the official Weblate catalogs while keeping confirmed local UI translations easy to edit.

## Start translating

1. Choose the `sync/vX.Y` branch matching your DSW minor release.
2. Open `translations/README.md` on that branch.
3. Choose an English source from the **Open** section and edit its `Translation (zh_Hant)` block in
   GitHub.
4. Open a pull request to the same version branch.

Each translation is a Markdown form. You do not need to edit PO files, write code, install tools, or
run a local Weblate server. CI validates the form, builds the locale, and provides screenshot
artifacts. Add the `live-preview` label to a pull request when you want a temporary browsable,
read-only DSW.

If the English text has no form, use an
[issue template](https://github.com/ThreeMonth03/dsw-ui-locales-zh_Hant/issues/new/choose) with the
DSW version, screen location, exact source text, and a screenshot.

Read the [contributor guide](CONTRIBUTING.md) or the
[translation website](https://www.threemonth03.com/dsw-ui-locales-zh_Hant/) for the complete workflow.

## Version branches

One `sync/vX.Y` branch is maintained for each release marked `active` or `maintenance` in
[`translation-config.yml`](translation-config.yml). These branches remain open for translation and
are not archived. New official Weblate release lines are added automatically when their source
catalogs become available.

`main` contains shared policy and documentation. Translation forms live only on version branches.
