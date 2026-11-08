# Technical Overview

The middleware maintains token buckets in Redis keyed by API key. Requests consume tokens and rejected requests receive a retry-after hint derived from the bucket refill rate.
