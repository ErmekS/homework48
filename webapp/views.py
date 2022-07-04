from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from webapp.forms import ProductForm
from webapp.models import Product, CATEGORY_CHOICES


def index_view(request):
    products = Product.objects.order_by("category")
    context = {"products": products}
    return render(request, "index.html", context)


def product_view(request, **kwargs):
    pk = kwargs.get("pk")
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_view.html", {"product": product})


def create_product(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "create.html", {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get("product_name")
            description = form.cleaned_data.get("description")
            category = form.cleaned_data.get("category")
            balance = form.cleaned_data.get("balance")
            price = form.cleaned_data.get("price")
            new_product = Product.objects.create(product_name=product_name, description=description, category=category,
                                                 balance=balance, price=price)
            return redirect("product_view", pk=new_product.pk)
        return render(request, "create.html", {"form": form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        form = ProductForm(initial={
            "product_name": product.product_name,
            "description": product.description,
            "category": product.category,
            "balance": product.balance,
            "price": product.price,
        })
        return render(request, "update.html", {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.product_name = form.cleaned_data.get("product_name")
            product.description = form.cleaned_data.get("description")
            product.category = form.cleaned_data.get("category")
            product.balance = form.cleaned_data.get("balance")
            product.price = form.cleaned_data.get("price")
            product.save()
            return redirect("product_view", pk=product.pk)
        return render(request, "update.html", {"form": form})
