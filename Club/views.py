from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting, MeetingMinute

# Create your views here.
def index(request): 
    return render(request,  'Club/index.html')

def resources(request):
    resource_list=Resource.objects.all()#bad for big lists, use find instead
    return render(request, 'Club/resources.html', {'resource_list': resource_list})

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meeting_list':meeting_list})

def meetingDetails(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    # date=meeting.meetingDate
    # time=meeting.meetingTime
    # locat=meeting.meetingLocation
    minute=MeetingMinute.objects.get(meetingID=meeting.id)
    context={
        'meeting' : meeting,
        # 'date' : date,
        # 'time' : time,
        # 'locat' : locat,
        'minute': minute,
    }
    return render(request, 'Club/meetingDetails.html', {'meeting': meeting, 'minute' : minute})