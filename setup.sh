#!/bin/bash
python manage.py makemigrations
python manage.py migrate

echo "Creating Django superuser..."
python manage.py createsuperuser --username=admin --email=admin@example.com --noinput

echo "Setting superuser password..."
python manage.py shell << EOF
from django.contrib.auth.models import User
user = User.objects.get(username='admin')
user.set_password('admin')
user.save()
EOF

echo "Superuser 'admin' created with password 'admin'"

python manage.py runserver
