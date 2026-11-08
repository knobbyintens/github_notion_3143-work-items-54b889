# Technical Overview

Jobs are enqueued into per-priority queues and dispatched to a worker pool. Starvation is avoided by aging jobs that wait beyond a threshold into a higher priority class.
