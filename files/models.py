from django.db import models

class Object (models.Model):
    file = models.FileField()
