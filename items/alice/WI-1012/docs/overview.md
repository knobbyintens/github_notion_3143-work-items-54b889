# Technical Overview

The export service streams rows from the primary warehouse into a temporary object store, then hands the archive to the download gateway. Cursors are checkpointed so an interrupted export can resume without re-reading the whole table.
