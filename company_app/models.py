from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):
    name = models.CharField(max_length=200, db_index=True)
    position = models.CharField(max_length=200, db_index=True)
    hire_date = models.DateField(db_index=True)
    email = models.EmailField(db_index=True)
    parent = TreeForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return f"{self.name} ({self.position})"


class User(AbstractUser):
    image = models.ImageField(upload_to="images/")
