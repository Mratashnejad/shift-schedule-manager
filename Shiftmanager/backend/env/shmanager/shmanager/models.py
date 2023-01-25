#data base will located here


from django.db import models
from ics import Calendar,Event
import datetime
from pytz import timezone

class Shift(models.Model):

    name                   = models.CharField(max_length=20)
    start_time             = models.TimeField
    end_time               = models.TimeField

    def __str__(self):
        return self.name


class Schadule(models.Model):

    start_date              = models.DateField()
    tz                      = timezone("Asia/Yerevan")

    def create_iCalander(self):
        cal = Calendar()

        morning_shift       = Shift.objects.name("Morning Shift")
        evening_shift       = Shift.objects.name("Evening Shift")
        night_shift         = Shift.objects.name("Night Shift")
        
        for i in range(52):
            #Create morning shift event
            morning = Event()
            morning.name    = "Morning Shift"
            morning.begin   = datetime.datetime.combine(self.start_date + datetime.timedelta(days=i * 7),morning_shift.start_time,self.tz)
            morning.end     = datetime.datetime.combine(self.end_time + datetime.timedelta(days=(i * 7)+1),morning_shift.end_time,self.tz )
            #Create evening shift event 
            evening = Event()
            evening.name    = "Evening Shift"
            evening.begin   = datetime.datetime.combine(self.start_date + datetime.timedelta(days= (i * 7)+ 2),evening_shift.start_time , self.tz)
            evening.end     = datetime.datetime.combine(self.end_time + datetime.timedelta(days=(i * 7)+3),evening_shift.end_time,self.tz)

            #create night shift  event
            night = Event()
            night.name      = "Night Shift"
            night.begin     = datetime.datetime.combine(self.start_date + datetime.timedelta(days=(i*7) + 4 ), night_shift.start_time,self.tz)
            night.end       = datetime.datetime.combine(self.end_time + datetime.timedelta(days=(i * 7)+ 5),night_shift.end_time,self.tz)

