from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SaleSearchForm
import pandas as pd


# Create your views here.
def home_view(request):
    form = SaleSearchForm(request.POST or None)

    if request.method == "POST":
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        chart_type = request.POST.get("chart_type")

        qs = Sale.objects.filter(created__range=(date_from, date_to))
        df1 = pd.DataFrame(qs.values())
        print(df1)

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
