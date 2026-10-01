# Version branches

| Branch | Purpose |
| --- | --- |
| `main` | Shared contributor instructions, workflow pins, and configuration |
| `sync/vX.Y` | Official catalogs and Markdown translation forms for one DSW minor version |

The daily synchronization discovers official Weblate versions and creates a branch once the
matching official source catalogs are available. Existing branches remain maintained, including
versions whose official Weblate project is locked.

Each version is synchronized independently. This tool does not automatically overwrite another
version's translations. Weblate remains responsible for its own cross-component propagation.

There is no local locale package version or container release.
The upstream source commit and translation Git history provide the revision record.
