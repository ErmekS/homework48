from django import forms
from django.forms import widgets

CATEGORY_CHOICES = [('other', 'Разное'), ('grocery', 'Бакалея'), ('confectionery', 'Кондитерка'), ('gastronomy', 'Гастрономия'), ('drinks', 'Напитки')]

class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=50, required=True, label='Наименование товара')
    description = forms.CharField(max_length=2000, required=False, label='Описание товара', widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))
    category = forms.ChoiceField(required=True, choices=CATEGORY_CHOICES, label="Категория")
    balance = forms.IntegerField(min_value=1, label="Остаток")
    price = forms.DecimalField(max_digits=7, decimal_places=2, label="Цена")







