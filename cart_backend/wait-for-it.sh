#!/bin/bash
host="$1"
port="$2"
shift 2
cmd="$@"

until nc -z "$host" "$port"; do
  echo "Waiting for database to be ready..."
  sleep 1
done

echo "Database is ready, starting app..."
exec $cmd
