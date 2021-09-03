from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class mymodel(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    material = models.CharField(max_length=100)

    msg = models.TextField(100)

    pics = models.FileField(upload_to='image/', max_length=100, null=True, blank=True)



    def __str__(self):
        return self.name

