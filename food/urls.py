from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='food_index'),
    path('index.html', views.index, name='food_index_html'),
    path('order/', views.order_view, name='food_order'),
    path('add-to-basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('update-basket/<int:product_id>/<str:action>/', views.update_basket, name='update_basket'),
    path('remove-basket/<int:product_id>/', views.remove_from_basket, name='remove_basket'),
]
