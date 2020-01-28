from django.conf import settings
from django.db import models


class Tesla(models.Model):
    "Generated Model"
    color = models.TextField()
    releaseDate = models.DateField(null=True, blank=True,)
    price = models.DecimalField(
        max_digits=30, decimal_places=10, null=True, blank=True,
    )


# Create your models here.
