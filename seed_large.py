import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from dashboard.models import Category, Product

def seed_more():
    # 1. Kategoriyalarni aniqlash
    pitsa, _ = Category.objects.get_or_create(name="Pitsalar")
    burger, _ = Category.objects.get_or_create(name="Burgerlar")
    kombo, _ = Category.objects.get_or_create(name="Kombo")
    ichimlik, _ = Category.objects.get_or_create(name="Ichimliklar")
    salat, _ = Category.objects.get_or_create(name="Salatlar")

    # 2. Mahsulotlar to'plami
    products_data = [
        # Pitsalar
        {"name": "Gavaya Pitsasi", "price": 45000, "cat": pitsa, "img": "assets/img/pitza1.png"},
        {"name": "Mexica Pitsasi", "price": 53000, "cat": pitsa, "img": "assets/img/pitza2.png"},
        {"name": "Margarita", "price": 42000, "cat": pitsa, "img": "assets/img/pitza3.png"},
        {"name": "Pepperoni", "price": 48000, "cat": pitsa, "img": "assets/img/pitza4.png"},
        {"name": "Go'shtli Pitsa", "price": 60000, "cat": pitsa, "img": "assets/img/pitza5.png"},
        {"name": "Qo'ziqorinli Pitsa", "price": 45000, "cat": pitsa, "img": "assets/img/pitza6.png"},
        
        # Burgerlar
        {"name": "Gamburger", "price": 25000, "cat": burger, "img": "assets/img/burger.png"},
        {"name": "Cheeseburger", "price": 28000, "cat": burger, "img": "assets/img/burger.png"},
        {"name": "Chili Burger", "price": 26000, "cat": burger, "img": "assets/img/burger.png"},
        {"name": "Double Burger", "price": 35000, "cat": burger, "img": "assets/img/burger.png"},
        {"name": "Big Max Burger", "price": 32000, "cat": burger, "img": "assets/img/burger.png"},
        
        # Kombo
        {"name": "Kombo-1 (Burger+Cola+Fri)", "price": 35000, "cat": kombo, "img": "assets/img/kombo1.png"},
        {"name": "Kombo-2 (Pitsa+Fanta)", "price": 55000, "cat": kombo, "img": "assets/img/kombo2.png"},
        {"name": "Student Kombo", "price": 22000, "cat": kombo, "img": "assets/img/kombo1.png"},
        
        # Ichimliklar
        {"name": "Coca-Cola 1.5L", "price": 12000, "cat": ichimlik, "img": "assets/img/cola.png"},
        {"name": "Fanta 1.5L", "price": 12000, "cat": ichimlik, "img": "assets/img/fanta.png"},
        {"name": "Sprite 1L", "price": 9000, "cat": ichimlik, "img": "assets/img/sprite.png"},
        {"name": "Choy (Limonli)", "price": 5000, "cat": ichimlik, "img": "assets/img/cola.png"},
        
        # Salatlar
        {"name": "Sezar Salati", "price": 18000, "cat": salat, "img": "assets/img/pict1.png"},
        {"name": "Karamli Salat", "price": 10000, "cat": salat, "img": "assets/img/pict2.png"},
    ]

    for p in products_data:
        prod, created = Product.objects.get_or_create(
            name=p['name'],
            category=p['cat'],
            defaults={'price': p['price']}
        )
        # Rasmni statik assets'dan olish (agar rasm bazada bo'lmasa)
        # Eslatma: Real loyihada rasm media papkasida bo'lishi kerak, 
        # lekin biz hozir assets'dan ko'rsatish mantiqini index_1 da qoldiramiz.

    print("Mahsulotlar muvaffaqiyatli qo'shildi!")

if __name__ == "__main__":
    seed_more()
