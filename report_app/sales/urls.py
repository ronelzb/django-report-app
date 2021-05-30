from django.urls import path
from .views import home_view
from .views import (
    home_view,
    SaleListView,
    SaleDatailView
)


app_name = "sales"

urlpatterns = [
    path("", home_view, name="home"),
    path("sales/", SaleListView.as_view(), name="list"),
    path("sales/<pk>/", SaleDatailView.as_view(), name="detail")
]
