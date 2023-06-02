from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=date.today())
    estimated_end = models.DateTimeField(default=date.today())
    priority = models.IntegerField(default=3)

    def __str__(self):
        return self.title
