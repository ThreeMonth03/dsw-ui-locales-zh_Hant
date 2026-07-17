# Translator guide

## Fill a blank form

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

CI builds the pull request into a locale ZIP. A preview workflow can import that ZIP into a
disposable DSW installation and upload screenshots plus a report of visible English UI text. See the
[preview guide](https://www.threemonth03.com/dsw-locale-tool/preview.html) for artifact details.
