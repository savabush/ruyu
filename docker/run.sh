#!/bin/bash

run {
    python manage.py migrate

    python manage.py collectstatic --noinput

    uvicorn ruyu.asgi:application --host 0.0.0.0 --port 8000 --reload
}

run