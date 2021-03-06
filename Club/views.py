from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting, MeetingMinute
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

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
    minute=MeetingMinute.objects.get(meetingID=meeting.id)
    attendance=MeetingMinute.objects.only("meetingID", "minutes").only("attendance")
    context={
        'meeting' : meeting,
        'minute': minute,
        'attendace' : attendance
    }
    return render(request, 'Club/meetingDetails.html', {'meeting': meeting, 'minute' : minute, 'attendace' : attendance})

@login_required
def newMeeting(request):
    form = MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()

    else:
        form=MeetingForm()
    return render(request, 'Club/newmeeting.html', {'form': form})

@login_required
def newResource(request):
    form = ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()

    else:
        form=ResourceForm()
    return render(request, 'Club/newresource.html', {'form': form})

def loginmessage(request):
    return render(request, 'Club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'Club/logoutmessage.html')