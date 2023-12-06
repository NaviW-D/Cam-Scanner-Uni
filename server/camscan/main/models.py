from django.db import models

# Create your models here.


class CarTag(models.Model):
    tag = models.TextField(max_length=8)
    availability = models.BooleanField()
    #times data
    register_time = models.DateTimeField( auto_now_add=True)
    expiration_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.tag
