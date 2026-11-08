# Technical Overview

The probe reports process liveness separately from readiness. Readiness verifies the database connection and the outbound queue before the instance is marked available for traffic.
