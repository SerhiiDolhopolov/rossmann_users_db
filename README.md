<!-- omit in toc -->
## Languages
[![python](https://img.shields.io/badge/python-3.11-d6123c?color=white&labelColor=d6123c&logo=python&logoColor=white)](https://www.python.org/)

## Frameworks
[![sqlalchemy](https://img.shields.io/badge/sqlalchemy-2.0.41-d6123c?color=white&labelColor=d6123c&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)

## Services
[![docker](https://img.shields.io/badge/docker-d6123c?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![postgreSQL](https://img.shields.io/badge/postgresql-d6123c?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

<!-- omit in toc -->
## Table of Contents

## Introduction
🟢 **This is part 4 of 7 Docker sections in the 🔴 [Supermarket Simulation Project](https://github.com/SerhiiDolhopolov/rossmann_services).**

🔵 [**<- Previous part with Offline markets.**](https://github.com/SerhiiDolhopolov/rossmann_offline_markets)

## Project workflow
This section contains a User DB to show the possibility of interaction between API and clients. This section can be skipped as it contains a very small and uninteresting database.

## Docker Containers
**This Docker section includes:**
  - **User DB**
    - Server for Adminer:
      - `users_db:5432`
    - Server for external tools:
      - `localhost:4000`
    - Other:
      - `admin`
  - **App**

## Getting Started
**To start:**
1. Complete all steps in the [first part](https://github.com/SerhiiDolhopolov/rossmann_services).
2. Run the services:
```bash
docker compose up --build
```

## Next Section of the Project

[Rossmann API](https://github.com/SerhiiDolhopolov/rossmann_api)