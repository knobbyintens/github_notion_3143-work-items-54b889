# Technical Overview

Outbound webhook deliveries are retried with exponential backoff and jitter. After the configured attempt limit the payload is placed on a dead-letter queue for manual inspection.
