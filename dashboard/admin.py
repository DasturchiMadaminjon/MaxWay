from django.contrib import admin
from .models import Category, Product, Order, OrderProduct, Branch, Employee

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['category']

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'phone', 'total_price', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    inlines = [OrderProductInline]

admin.site.register(Branch)
admin.site.register(Employee)
