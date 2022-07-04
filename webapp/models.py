from django.db import models

# Create your models here.
CATEGORY_CHOICES = [('other', 'Разное'), ('grocery', 'Бакалея'), ('confectionery', 'Кондитерка'), ('gastronomy', 'Гастрономия'), ('drinks', 'Напитки')]


class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False, default="No Product", verbose_name="Наименование товара")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание товара")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name="Категория")
    balance = models.IntegerField(verbose_name="Остаток")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")


    def __str__(self):
        return f"{self.id}. {self.product_name}: {self.category} {self.balance} {self.price}"

    class Meta:
        db_table = "product"
        verbose_name = "товар"
        verbose_name_plural = "Список товаров"
