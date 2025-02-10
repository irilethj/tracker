from django.db import models
from django.utils import timezone as tz
from datetime import timedelta


class Task(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=255, unique=True, verbose_name="название задачи")
    start_time = models.DateTimeField(default=tz.now)
    duration_seconds = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    @property
    def state(self):
        state = {
            'active': 'в работе',
            'completed': 'завершена',
            'paused': 'на паузе'
        }
        return state[self.status]

    @property
    def time_spent(self):
        if self.status == 'completed':
            return '-'
        if self.status == 'paused':
            return str(self.duration)
        if self.duration:
            return str((tz.now() - self.start_time) + self.duration).split('.')[0]
        return str(tz.now() - self.start_time).split('.')[0]

    @property
    def duration(self):
        return timedelta(seconds=self.duration_seconds) if self.duration_seconds else None

    @property
    def total_time(self):
        if self.status == 'completed':
            return self.duration
        return '-'

    def update_duration(self):
        if not self.duration_seconds:
            self.duration_seconds = 0
        self.duration_seconds += (tz.now() - self.start_time).total_seconds()

    def mark_as_completed(self):
        self.update_duration()
        self.status = 'completed'
        self.save()

    def mark_as_paused(self):
        self.update_duration()
        self.status = 'paused'
        self.save()

    def mark_as_active(self):
        self.start_time = tz.now()
        self.status = 'active'
        self.save()

    def __str__(self):
        return self.name
