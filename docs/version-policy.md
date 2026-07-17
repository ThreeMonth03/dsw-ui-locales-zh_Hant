# Version branches

Every supported DSW minor release has an independent `sync/vX.Y` branch containing the exact
official source catalogs and its own Markdown translation forms.

| Branch | Purpose |
| --- | --- |
| `main` | Shared documentation, glossary, issue forms, and version configuration |
| `sync/vX.Y` | Translation work for one DSW minor release |

Versions 4.29, 4.30, 4.31, and 4.32 all remain open for contributions. A locked official Weblate
project is treated as a maintained release, not an archived one.

Automation adds a new version only after both its official Weblate project and `wizard-locales`
branch exist. It creates blank forms from that version's exact sources; translations are not copied
from another version by similarity.

When contributing, always target the same version branch where you found the form. After a pull
request is merged, automation fills matching blank forms on other maintained branches only when the
component, source, plural source, context, and form kind are identical. Existing translations are
never replaced. Automation also advances the immutable locale package version on every branch whose
effective translation content changed.
