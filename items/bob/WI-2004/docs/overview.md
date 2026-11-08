# Technical Overview

Uploads are streamed to a quarantine bucket, checked by the scanning hook and only then promoted to the public bucket. Size and content type limits are enforced before the stream is accepted.
