import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '1')
    print("Admin created (pass: 1)")
else:
    u = User.objects.get(username='admin')
    u.set_password('1')
    u.save()
    print("Admin password updated (pass: 1)")
