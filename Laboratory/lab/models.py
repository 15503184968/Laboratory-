from django.db import models

# Create your models here.
# class User(model.Model):
from django.db import models

class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username