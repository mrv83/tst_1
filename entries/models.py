import datetime

from django.contrib.auth.models import User
from django.db import models


class Entry(models.Model):
    user = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()
    statistic_record = models.ForeignKey('entries.Statistic', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.get_full_name()}: {self.date}'

    def save(self, *args, **kwargs):
        obj_before_saving = Entry.objects.get(pk=self.pk) if self.pk else None
        if not self.statistic_record:
            monday = self.date - datetime.timedelta(days=self.date.weekday())
            sunday = monday + datetime.timedelta(days=6)
            self.statistic_record, _ = Statistic.objects.get_or_create(
                user=self.user,
                week_number=datetime.date(self.date.year, self.date.month, self.date.day).isocalendar()[1],
                year=self.date.year,
                start=monday,
                end=sunday
            )
        super().save(*args, **kwargs)

        if obj_before_saving is None:
            self.statistic_record.amount_entries += 1
            self.statistic_record.total_duration += self.duration
            self.statistic_record.total_distance += self.distance
        else:
            self.statistic_record.total_distance += self.distance - obj_before_saving.distance
            self.statistic_record.total_duration += self.duration - obj_before_saving.duration
        self.statistic_record.save()

    def delete(self, using=None, keep_parents=False):
        self.statistic_record.amount_entries -= 1
        self.statistic_record.total_duration -= self.duration
        self.statistic_record.total_distance -= self.distance
        self.statistic_record.save()
        super().delete(using=using, keep_parents=keep_parents)


class Statistic(models.Model):
    user = models.ForeignKey(User, related_name='statistic', on_delete=models.CASCADE)
    week_number = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    start = models.DateField()
    end = models.DateField()
    amount_entries = models.PositiveIntegerField(default=0)
    total_duration = models.PositiveIntegerField(default=0)
    total_distance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.get_full_name()}: {self.week}'

    @property
    def week(self):
        return f'{self.start} - {self.end}'
