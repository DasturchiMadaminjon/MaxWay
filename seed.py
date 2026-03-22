import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from mainapp.models import Category, Branch, MenuItem, Employee, TableItem
from django.contrib.auth.models import User

# 1. Create or Update Superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '1')
    print("Superuser 'admin' created (pass: 1)")
else:
    u = User.objects.get(username='admin')
    u.set_password('1')
    u.save()
    print("Superuser 'admin' password updated (pass: 1)")

# 2. Add Sample Data
# Categories
cats = [
    Category.objects.get_or_create(name='Burgerlar', icon='fas fa-hamburger')[0],
    Category.objects.get_or_create(name='Salatlar', icon='fas fa-leaf')[0],
    Category.objects.get_or_create(name='Ichimliklar', icon='fas fa-glass-whiskey')[0],
]

# Branches
branch = Branch.objects.get_or_create(name='Tshkent, Chilonzor', address='Qatortol ko\'chasi', phone='+998901234567')[0]

# Menu Items
MenuItem.objects.get_or_create(name='Max Burger', price=35000, category=cats[0])
MenuItem.objects.get_or_create(name='Chizburger', price=28000, category=cats[0])
MenuItem.objects.get_or_create(name='Gretskiy salat', price=22000, category=cats[1])
MenuItem.objects.get_or_create(name='Coca-Cola 0.5', price=10000, category=cats[2])

# Tables
TableItem.objects.get_or_create(name='Stol #1', capacity=4, branch=branch)
TableItem.objects.get_or_create(name='Stol #2', capacity=6, branch=branch)

# Employees
Employee.objects.get_or_create(first_name='Anvar', last_name='Ismoilov', age=25, role='cashier', branch=branch)

print("Sample data added successfully.")
