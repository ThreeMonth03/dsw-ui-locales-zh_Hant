# Translator guide

## Translate or correct a form

Open `translations/README.md` on the matching version branch. Forms that still need work are listed
first under **Open**; completed forms remain below under **Completed**.

Prioritize empty fields and review the newly added translations. Keep existing
wording unless a problem has been identified. Existing translations are not
archived or frozen: address reported issues in focused PRs, link the report or
discussion, and explain the correction. This includes nonempty fuzzy entries.
Avoid unrelated rewrites and do not edit generated PO files or review flags.

CI validates source identity, formatting, and placeholders for both new
translations and corrections. Official Weblate sync continues independently.
If the official translation has no Markdown form, report the issue so a
maintainer can prepare a form from its official POT entry.

A translation form looks like this:

````markdown
## Source (en)
~~~text
Save changes
~~~

## Translation (zh_Hant)
~~~text

~~~
````

Enter the translation between the second pair of fences:

````markdown
## Translation (zh_Hant)
~~~text
儲存變更
~~~
````

Leave every other part of the file unchanged. For plural sources, one Traditional Chinese block is
used because this locale has one gettext plural form.

## Translation guidelines

- Follow `glossary/zh-Hant.csv` for established terms.
- Preserve `%s`, `{name}`, `${value}`, and similar placeholders exactly.
- Preserve Markdown links and formatting when they are part of the source message.
- Use the screenshot or UI context instead of translating an ambiguous source in isolation.
- Keep product names, identifiers, and standard abbreviations unchanged unless the glossary says
  otherwise.

## Metric terminology

Use `權重` for `Weight` and `衡量值` for `Measure`. In the Knowledge Model answer
editor, weight expresses an answer's importance and measure expresses its
evaluation for a metric. The project's Metrics page displays the aggregated
measure. Keep the labels consistent across both screens; do not change the
underlying values or scoring rules.

FAIR metric names and descriptions belong to the Knowledge Model locale, not
the UI locale. Correct them in the KM translation repository.

## See the translation in DSW

CI builds every non-draft translation pull request and imports it into a disposable DSW
installation. After validation, a **DSW locale preview** comment shows that rendering has started.
The same comment links to the screenshots and visible English-text report when the
**Render DSW preview** check finishes. See the
[preview guide](https://www.threemonth03.com/dsw-locale-tool/preview.html) for artifact details.
The installation includes the maintained Traditional Chinese DepositAR Knowledge Model and Science
Europe document template, so the questionnaire and document screens use real localized content.

For an interactive review, ask a maintainer to add the `live-preview` label to the pull request.
Contributors with label permission may add it directly. A **DSW translation live preview** comment
will receive a temporary HTTPS link after the isolated DSW is ready. Open the link, sign in with the
account shown on its landing page, and use the listed review pages. The site contains sample data,
and actions that would change DSW data are blocked.

The live preview ends after 30 minutes without browser activity and always ends after three hours.
A new translation commit replaces the current preview with one built from the new commit. Remove
the label to stop it early. To start another preview after one expires, remove and reapply the
label. Screenshot artifacts remain available after the live site closes.
