# DSW UI Traditional Chinese Translations

Contribute Traditional Chinese translations to official DSW Weblate using Markdown forms.

## Start translating

1. Choose the `sync/vX.Y` branch matching the DSW version.
2. Open `translations/README.md` and choose an empty translation.
3. Fill only the `Translation (zh_Hant)` block.
4. Open a pull request to the same version branch.

No programming, PO editing, or local installation is required.
CI checks the source identity and placeholders. Maintainers submit reviewed batches to official
Weblate as fuzzy translations for further review. Merging a PR does not itself upload or approve it.

Use existing translations as the terminology baseline; consult the glossary when needed.
Leave existing wording unchanged unless a problem is reported, then propose a focused correction.

Read [CONTRIBUTING.md](CONTRIBUTING.md) or the
[translation guide](https://www.threemonth03.com/dsw-ui-locales-zh_Hant/).

## Official source and versions

The official Weblate catalogs and linked
[wizard-locales repository](https://github.com/ds-wizard/wizard-locales) define the available strings.
We do not extract frontend strings or maintain a separate DSW interface.

`main` contains shared instructions and configuration.
Each `sync/vX.Y` branch contains official snapshots and translation forms for that release.
Automation discovers new official versions; existing versions remain maintained.

GitHub Pages provides contributor documentation, not a running DSW preview.
