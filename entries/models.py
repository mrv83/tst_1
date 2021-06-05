from django.contrib.auth.models import User
from django.db import models


class Entry(models.Model):
    user = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField()
    distance = models.IntegerField()

    def __str__(self):
        return f'{self.user.get_full_name()}: {self.date}'
