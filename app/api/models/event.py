from djongo import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
