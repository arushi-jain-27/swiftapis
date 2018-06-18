from django.db import models

class Container (models.Model):
    name = models.CharField (max_length=30)
    def __str__(self):
        return self.name

class Object (models.Model):
    name = models.CharField (max_length=30)
    container = models.ForeignKey(Container, on_delete = models.CASCADE)
    file_url = models.CharField (max_length=200 )
    def __str__(self):
        return self.name

# Create your models here.
