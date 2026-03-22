from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {"name": forms.TextInput(attrs={'class': 'form-control'})}

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "category": forms.Select(attrs={'class': 'form-control'}),
        }
class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"
class TableForm(forms.ModelForm):
    class Meta:
        model = TableItem
        fields = "__all__"
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"