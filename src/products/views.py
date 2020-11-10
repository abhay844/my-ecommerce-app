from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
# Create your views here.


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/list.html", context)

