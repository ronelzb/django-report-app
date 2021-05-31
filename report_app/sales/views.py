from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SaleSearchForm


# Create your views here.
def home_view(request):
    form = SaleSearchForm(request.POST or None)
    context = {
        "form": form
    }
    return render(request, "sales/home.html", context)


class SaleListView(ListView):
    model = Sale
    template_name = "sales/main.html"


class SaleDatailView(DetailView):
    model = Sale
    template_name = "sales/detail.html"
