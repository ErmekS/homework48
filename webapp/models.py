from django.db import models

# Create your models here.
CATEGORY_CHOICES = [('other', 'Разное'), ('grocery', 'Бакалея'), ('confectionery', 'Кондитерка'), ('gastronomy', 'Гастрономия'), ('drinks', 'Напитки')]


class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False, default="No Product", verbose_name="Наименование товара")
    entry = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Запись")
    email = models.EmailField(max_length=20, null=False, blank=False, default="No Email", verbose_name="Email автора")

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                              verbose_name="Категория")

    def __str__(self):
        return f"{self.id}. {self.entry}: {self.status} {self.author} {self.email}"

    class Meta:
        db_table = "product"
        verbose_name = "товар"
        verbose_name_plural = "Список товаров"
