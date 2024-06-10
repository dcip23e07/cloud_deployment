from django.db import models

from todo.constants import (
    STATUS_CHOICES,
    COLOR_CHOICES,
    PRIORITY_CHOICES
)

class ToDo(models.Model):
    scheduled_at = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(default=0)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='notstarted')
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='black')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='low')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)