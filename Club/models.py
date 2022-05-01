from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.TimeField()
    meetingLocation=models.CharField(max_length=255)
    meetingAgenda=models.TextField()

    def __str__(self):
        return self.meetingTitle

    class Meta:
        db_table='meeting'

class MeetingMinute(models.Model):
    meetingID = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutes = models.TextField()

    def __str__(self):
        return self.meetingID
        
    class Meta:
        db_table='meetingMinute'
        verbose_name_plural='meetingMinutes'

class Resource(models.Model):
    resourceName = models.CharField(max_length=255)
    resourceType = models.CharField(max_length=255)
    resourceURL = models.URLField()
    dateEntered = models.DateField()
    posterUser = models.ForeignKey(User, on_delete=models.CASCADE)
    resourceDescription = models.TextField()

    def __str__(self):
        return self.resourceName
        
    class Meta:
        db_table='resource'

class Event(models.Model):
    eventTitle = models.CharField(max_length=255)
    eventLocation = models.CharField(max_length=255)
    eventDate = models.DateField()
    eventTime = models.TimeField()
    eventDescription = models.TextField()
    posterUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventTitle
        
    class Meta:
        db_table='event'