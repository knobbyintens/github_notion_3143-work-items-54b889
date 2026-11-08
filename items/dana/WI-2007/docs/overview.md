# Technical Overview

The adapter buffers rows into columnar batches and writes them as partitioned Parquet files partitioned by event date. Schema evolution is handled by merging the incoming schema with the declared target schema before each flush.
