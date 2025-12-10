from django.db import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.email


# Create your models here.
