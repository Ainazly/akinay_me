from django.db import models

# Create your models here.


class Menu(models.Model):
    meal_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.description} {self.meal_name}"


