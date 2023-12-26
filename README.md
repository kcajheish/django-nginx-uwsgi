# Introduction
It's a django, nginx and uwsgi stack template with Postgres and Redis. The whole environment is built in container so you can prototype idea without worrying about dependencies.

# Prerequisite
Install docker environment

# Getting Started
specify folder path for postgres volume in .env
```
DATABASE_VOLUME=<your postgres volume path>
```

create folder
```
mkdir <your postgres volume path>
```

orchestrate containers through
```
docker compose up
```

access to db in the container
```
docker exec -it <db container id> sh -c "psql -U postgres"
```

create database instance and leave it
```
CREATE DATABASE backend;
\q
```

migrate database schema
```
docker exec -it <backend container id> python manage.py migrate
```

create super user
```
docker exec -it <backend container id> python manage.py createsuperuser --username admin --email admin@example.com
```

collect static content
```
docker exec -it <backend container id> python manage.py collectstatic
```

verify the setup using curl
```
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/users/1/
```
