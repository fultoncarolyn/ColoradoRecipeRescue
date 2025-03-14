# Capstone Starter

A capstone starter application. 
* See public-facing URL here: ADD ONCE DEPLOYED - HOMEWORK 5
* For current project overview and architecture diagrams, see: https://github.com/coloradocollective/s25-team-6-capstone/wiki/Overview
* To see user stories we are working on, see: https://github.com/orgs/coloradocollective/projects/5/views/1

## Technology stack

This codebase is written [Python](https://www.python.org/) and uses [Flask](https://flask.palletsprojects.com/) and
[Jinja2 Templates](https://jinja.palletsprojects.com/templates/).
It stores data in [PostgreSQL](https://www.postgresql.org/), and a [GitHub Action](https://github.com/features/actions)
runs tests.

## Architecture

The Capstone Starter consists of three free-running processes communicating with one Postgres database.

1. The data collector is a background process that collects data from one or more sources.
1. The data analyzer is another background process that processes collected data.
1. The web application displays results to the user.

## Local development

1. Install [uv](https://formulae.brew.sh/formula/uv) and [PostgreSQL 17](https://formulae.brew.sh/formula/postgresql@17).
   ```shell
   brew install uv postgresql@17
   brew services run postgresql@17
   ```

1. Set up environment variables.
   ```shell
   cp .env.example .env 
   source .env
   ```

1. Set up the database.
   ```shell
   psql postgres < databases/create_databases.sql
   uv run alembic upgrade head
   DATABASE_URL="postgresql://localhost:5432/capstone_starter_test?user=capstone_starter&password=capstone_starter" uv run alembic upgrade head
   ```

1. Run tests.
   ```shell
   uv run -m unittest
   ```

1. Run the collector and the analyzer to populate the database, then run the app and navigate to
   [localhost:5001](http://localhost:5001).
   ```shell
   uv run -m starter.collect
   uv run -m starter.analyze
   uv run -m starter
   ```

## Create a database schema migration

Use alembic to create a database schema migration.

```shell
uv run alembic revision -m "[Description of change]"
```

## Build container

1. Build container
   ```shell
   uv pip compile pyproject.toml -o requirements.txt
   docker build -t capstone-starter .
   ```

1. Run with docker
   ```shell
   docker run --env-file .env.docker --entrypoint ./collect.sh capstone-starter
   docker run --env-file .env.docker --entrypoint ./analyze.sh capstone-starter
   docker run -p 8081:8081 --env-file .env.docker capstone-starter
   ```   
