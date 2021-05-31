from datetime import datetime, timedelta
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

        qs = Sale.objects.filter(
            created__date__gte=datetime.strptime(date_from, "%Y-%m-%d").date(),
            created__date__lte=datetime.strptime(date_to, "%Y-%m-%d").date()
            + timedelta(days=1)
        )

        sales_df = None
        if len(qs) > 0:
            sales_df = pd.DataFrame(qs.values())
            sales_df = sales_df.to_html()
            print(sales_df)

    context = {
        "form": form,
        "sales_df": sales_df
    }
    return render(request, "sales/home.html", context)


class SaleListView(ListView):
    model = Sale
    template_name = "sales/main.html"


class SaleDatailView(DetailView):
    model = Sale
    template_name = "sales/detail.html"
