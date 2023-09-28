from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    sales_rep = models.CharField(max_length=20, null=True, blank=True, default=None)
    sales_rep_email = models.CharField(max_length=40, null=True, blank=True, default=None)

    def __str__(self):
        return self.username