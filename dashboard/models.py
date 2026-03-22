from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    def __str__(self): return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self): return self.name

class TableItem(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    def __str__(self): return f"{self.name} ({self.branch.name})"

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL)
    def __str__(self): return f"{self.first_name} {self.last_name}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    def __str__(self): return self.name

class Order(models.Model):
    STATUS = [('pending', 'Kutilmoqda'), ('ready', 'Tayyor'), ('delivered', 'Yetkazildi')]
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, null=True, blank=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Order #{self.id} - {self.customer_name}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class AuditLog(models.Model):
    user = models.ForeignKey("auth.User", null=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=32)
    entity = models.CharField(max_length=64)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
