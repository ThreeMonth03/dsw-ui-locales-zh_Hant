# Translator guide

## Fill a blank form

Open `translations/README.md` on the matching version branch. Forms that still need work are listed
first under **Open**; completed forms remain available below for corrections.

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
