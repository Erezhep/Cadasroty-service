from django.db import models

# Create your models here.

class Request(models.Model):
    cadastral_number = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    result = models.BooleanField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cadastral_number} - {self.timestamp}'
