from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code
from django.shortcuts import reverse
# Create your models here.


class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # Optional: To be updated automatically when the price from the Product is changed
    price = models.FloatField(blank=True)
    # Optional: To be managed by django admin
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"id: {self.id}, product: {self.product.name}, quantity: {self.quantity}"


class Sale(models.Model):
    # Optional: id overwritten by the save method in this class
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

    def get_absolute_url(self):
        return reverse("sales:detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"Sales for the amount of ${self.total_price}"


class CSV(models.Model):
    file_name = models.FileField(upload_to="CSVs")
    # if we used this file already
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.file_name)
