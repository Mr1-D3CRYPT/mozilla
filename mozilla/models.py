from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/') 
    description = models.TextField()

    def __str__(self):
        return self.name