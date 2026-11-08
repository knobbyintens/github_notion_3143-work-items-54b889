# Work Item Template

Every work item is a self-contained folder stored under
`items/<developer>/<work-item-id>/`.

Required files
--------------
- `README.md` - a short human-readable summary of the work item.
  It must be non-empty and written in English.
- `docs/overview.md` - the technical overview of the change.
  It must be non-empty and written in English.

Optional files
--------------
- `docs/notes.md` - supplementary notes. This file is optional.
- `evaluation/main.py` - an automated evaluation entry point. This file is
  optional; items whose behaviour does not need automated checks may omit it.
- `metadata/` - free-form auxiliary metadata. This folder is optional.

Everything not listed as required above is optional.
