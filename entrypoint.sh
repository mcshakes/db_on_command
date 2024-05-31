#!/bin/bash

# Ensure data directory exists
mkdir -p /var/lib/postgresql/data

# Set permissions for the data directory
chown -R postgres:postgres /var/lib/postgresql/data

# Execute the original entrypoint script with all passed arguments
exec /usr/local/bin/docker-entrypoint.sh "$@"
