# Technical Overview

The runner acquires an advisory lock, applies pending migrations in version order and records each applied version together with its checksum. A dry-run mode prints the plan without touching the schema.
