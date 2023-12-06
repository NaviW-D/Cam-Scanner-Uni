from django.db import models

# Create your models here.


class CarTag(models.Model):
    tag = models.TextField(max_length=8)
    availability = models.BooleanField()

    def __str__(self):
        return self.tag
