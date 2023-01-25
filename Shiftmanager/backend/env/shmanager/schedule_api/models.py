from django.db import models

# Create your models here.


class ScheduleEvent(models.Model):
    name        = models.CharField(max_length=20)
    start_date  = models.DateField()
    end_date    = models.DateField()

