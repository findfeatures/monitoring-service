#!/bin/bash

## Run Migrations
alembic upgrade head

# Run Service
nameko run --config config.yml monitoring.service:MonitoringService