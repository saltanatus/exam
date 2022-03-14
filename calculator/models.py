from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    first_number = models.IntegerField()
    balans_group = models.IntegerField()

    def __str__(self):
        return self.name


class Resource(models.Model):
    label = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_number = models.IntegerField()
    initial_cost = models.IntegerField()
    residual_cost = models.IntegerField()

    def __str__(self):
        return self.label
