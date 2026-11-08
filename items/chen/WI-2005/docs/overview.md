# Technical Overview

The cache wraps read-only queries with a key derived from the normalised statement and its bound parameters. Entries are invalidated by table-level version stamps.
