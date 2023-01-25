#web page will be here

from django.db import models
from ics import Calendar,Event
import datetime
from pytz import timezone

class Shift(models.Model):

    name       =            models.CharField(max_length=20)
    start_time =            models.TimeField
    end_time   =            models.TimeField

    def __str__(self):
        return self.name


class Schadule(models.Model):

    start_date =            models.DateField()
    tz         =            timezone("Asia/Yerevan")

    def create_iCalander(self):
        cal = Calendar()

        morning_shift       = Shift.objects.name("Morning Shift")
        evening_shift       = Shift.objects.name("Evening Shift")
        night_shift         = Shift.objects.name("Night Shift")
        





        morning = Event()
        morning_name = "Morning Shift"

        morning_begin = datetime.datetime.combine(self.start_date + datetime.timedelta(days=i+7)),morning_shift.start_time,self.tz)
