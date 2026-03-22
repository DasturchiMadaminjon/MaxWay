from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Category, Product, Order, OrderProduct
from django.http import JsonResponse

# 1. Savatga qo'shish (AJAX)
def add_to_basket(request, product_id):
    basket = request.session.get('basket', {})
    product_id = str(product_id)
    
    if product_id in basket:
        basket[product_id] += 1
    else:
        basket[product_id] = 1
        
    request.session['basket'] = basket
    return JsonResponse({'status': 'ok', 'count': sum(basket.values())})

# 1.1. Savatni yangilash (Miqdorini o'zgartirish)
def update_basket(request, product_id, action):
    basket = request.session.get('basket', {})
    product_id = str(product_id)
    
    if product_id in basket:
        if action == 'plus':
            basket[product_id] += 1
        elif action == 'minus':
            basket[product_id] -= 1
            if basket[product_id] < 1:
                del basket[product_id]
                
    request.session['basket'] = basket
    return redirect('food_order')

# 1.2. Savatdan o'chirish
def remove_from_basket(request, product_id):
    basket = request.session.get('basket', {})
    product_id = str(product_id)
    
    if product_id in basket:
        del basket[product_id]
        
    request.session['basket'] = basket
    return redirect('food_order')

# 2. Savat sahifasi (Checkout)
def order_view(request):
    basket = request.session.get('basket', {})
    products_in_basket = []
    total_price = 0
    
    for pid, qty in basket.items():
        product = get_object_or_404(Product, pk=pid)
        item_total = product.price * qty
        total_price += item_total
        products_in_basket.append({
            'product': product,
            'qty': qty,
            'total': item_total
        })
    
    if request.method == 'POST':
        # Buyurtmani bazaga yozish
        customer_name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        if customer_name and phone and basket:
            order = Order.objects.create(
                customer_name=customer_name,
                phone=phone,
                address=address,
                total_price=total_price
            )
            for item in products_in_basket:
                OrderProduct.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['qty'],
                    price=item['product'].price
                )
            # Savatni tozalash
            request.session['basket'] = {}
            return render(request, 'order_success.html', {'order': order})
            
    return render(request, 'order.html', {
        'items': products_in_basket,
        'total_price': total_price
    })

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    # Savatdagi narsalar soni
    basket_count = sum(request.session.get('basket', {}).values())
    return render(request, 'index_1.html', {
        'categories': categories, 
        'products': products,
        'basket_count': basket_count
    })
