#!/bin/sh

docker-compose down -v
rm -rf db.sqlite3
rm -rf account/migrations

docker-compose up -d --build

docker exec django_account python /workspace/django_account/manage.py makemigrations account
docker exec django_account python /workspace/django_account/manage.py migrate
docker exec django_account python /workspace/django_account/manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@mail', 'hogehoge')"
docker exec django_account python /workspace/django_account/manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_user('user@mail', 'hogehoge')"
