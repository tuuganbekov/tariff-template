from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="tariff")

    def __str__(self):
        return self.title
