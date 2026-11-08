# Technical Overview

Idempotency keys are stored with a TTL in the shared cache. A small in-process lock prevents duplicate inserts for the same key under concurrent requests, and expired keys are evicted lazily.
