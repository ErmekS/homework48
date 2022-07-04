from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'description', 'category', 'balance', 'price', 'created_time', 'updated_time']
    list_display_links = ['product_name']
    list_filter = ['category']
    search_fields = ['product_name']
    fields = ['product_name', 'category', 'balance', 'price', 'created_time', 'updated_time']
    readonly_fields = ['created_time', 'updated_time']


admin.site.register(Product, ProductAdmin)