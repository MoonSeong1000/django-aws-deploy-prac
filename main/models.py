from django.db import models
from django.utils import timezone


# Create your models here.
class Plan(models.Model):
    planId = models.IntegerField()
    name = models.TextField()
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    progressTime = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        Plan.objects.filter(date__lte=timezone.now()) \
            .order_by('date')
        return self.name


