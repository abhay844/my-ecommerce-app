from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404
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


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(id=pk)
        if instance is not None:
            return instance
        else:
            raise Http404("Product does not exist")


def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = get_object_or_404(Product, pk=pk)
    context = {}
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print("Product does not exist")
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("Something else")

    instance = Product.objects.get_by_id(id=pk)
    if instance is not None:
        context["object"] = instance
    else:
        raise Http404("Product does not exist")

    return render(request, "products/detail.html", context)

