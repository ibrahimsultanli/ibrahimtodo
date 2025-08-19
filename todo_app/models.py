from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50, choices=[
        ('personal', 'Şəxsi'),
        ('work', 'İş'),
        ('education', 'Təhsil'),
        ('other', 'Digər'),
    ], default='personal')

    def __str__(self):
        return self.title
