# Technical Overview

Counters are grouped into minute buckets and then folded into hourly rollups. Events that arrive after a bucket has been sealed are routed to a correction stream that amends the closed bucket on the next pass.
