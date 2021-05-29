from django.db import models
from django.db.models.deletion import CASCADE
from profiles.models import Profile


# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="reports", blank=True)
    remarks = models.TextField()
    author = models.ForeignKey(Profile, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)
    