import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from dashboard.models import Category, Product

# Kategoriya yaratish
cat1, _ = Category.objects.get_or_create(name="Burgerlar")
cat2, _ = Category.objects.get_or_create(name="Pitsalar")

# Mahsulot yaratish
Product.objects.get_or_create(name="Gamburger", price=25000, category=cat1)
Product.objects.get_or_create(name="Cheeseburger", price=28000, category=cat1)
Product.objects.get_or_create(name="Margarita 30cm", price=55000, category=cat2)

print("Namuna ma'lumotlari yuklandi!")
