# DSW UI Traditional Chinese translations

This repository provides a simple translation queue for English text missing from the official DSW
Traditional Chinese UI locale. Translation happens in Markdown files and can be completed entirely
in GitHub's web interface.

:::{admonition} Begin with a version branch
:class: tip

Choose the `sync/vX.Y` branch matching the DSW screen you are translating, then open
`translations/README.md` on that branch.
:::

```{toctree}
:maxdepth: 2
:hidden:

translator-guide
version-policy
```

## Contribution path

1. Open a blank translation form on the correct version branch.
2. Fill only the `Translation (zh_Hant)` block.
3. Submit a pull request to the same branch.
4. CI validates and packages the locale.
5. A disposable DSW preview renders the result for review.

If no form matches the UI text, use the repository's
[issue forms](https://github.com/ThreeMonth03/dsw-ui-locales-zh_Hant/issues/new/choose). Include the
DSW version, exact English text, screen location, and a screenshot.

The official `ds-wizard/wizard-locales` repository remains the baseline. When official Weblate adds
the same translation, automation removes the local form so this repository remains a focused work
queue.
