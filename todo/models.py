from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Creating a model for todo object
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)     # "blank=True" for optional field
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)  # default=False => since always not specified by the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)# 'Foreign Key'

    def __str__(self):
        return self.title