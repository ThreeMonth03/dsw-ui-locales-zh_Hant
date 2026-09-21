# Contributing translations

Use GitHub's web editor on the matching `sync/vX.Y` branch.
Open `translations/README.md`, select an empty form, and edit only its translation block.

````markdown
## Translation (zh_Hant)
~~~text
Enter the Traditional Chinese translation here.
~~~
````

Do not change the English source, context, hidden metadata, or fences.
Preserve placeholders such as `%s`, `{name}`, and `${value}`, and preserve Markdown links.
Use the surrounding interface to understand the wording.

Existing translations take precedence over the glossary when they conflict.
If neither resolves a term, ask for clarification in the PR.
For UI text, distinguish a DSW system project from a research project; do not mechanically
replace every instance of「專案」with「計畫」.

## Review

Prioritize empty translations. Existing wording is maintained, not frozen:
propose a focused correction when a problem is reported, and link the discussion.
Avoid unrelated rewrites.

CI checks source identity and placeholders. You do not need to update the generated index or
any version number. A maintainer submits reviewed batches to official Weblate with fuzzy status.
Official review happens on Weblate; PR merge is not approval or automatic upload.

## Report a missing form

Provide the DSW version, exact English text, screen context, and a screenshot if useful.
A maintainer can create a form for an existing official POT entry that needs correction.
A string absent from the official POT needs an upstream extraction fix, not a local workaround.

Knowledge Model questions and Document Template prose belong to their own translation projects.

## License

Translation contributions are published under CC BY 4.0.
