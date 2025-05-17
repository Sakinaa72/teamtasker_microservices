#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE taskservice;
    CREATE DATABASE authservice;
    CREATE DATABASE notificationservice;
    CREATE DATABASE userservice;
EOSQL