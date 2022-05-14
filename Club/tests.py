from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinute, Resource, Event
import datetime
# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.meeting=Meeting(meetingTitle="New Meeting", meetingDate=datetime.date(2021, 1, 1), meetingTime=datetime.time(12,0,0,0), meetingLocation="test location", meetingAgenda="lorem ipsum")

    def test_meetingstring(self):
        self.assertEqual(str(self.meeting), "New Meeting")  

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinuteTest(TestCase):
    def setUp(self):
        self.id=Meeting(meetingTitle="New Meeting")
        self.user=User(username='Louis')
        ## I had to change my models.MeetingMinute so that the meeting attendance could accept blank as I couldn't figure out how to generate/set the manytomany field in this test code :(
        ##I kept getting "Direct assignment to the forward side of a many-to-many set is prohibited. Use attendance.set() instead." and wasn't able to troubleshoot
        self.meetingminutes=MeetingMinute(meetingID = self.id, minutes="Test")

    def test_string(self):
        self.assertEqual(str(self.meetingminutes), "New Meeting minutes")  

    def test_tablename(self):
        self.assertEqual(str(MeetingMinute._meta.db_table), 'meetingMinute')

class ResourceTest(TestCase):
    def setUp(self):
        self.posteruser=User(username='user1')
        self.resource=Resource(resourceName="ResourceA", resourceType="TypeA", resourceURL='http://www.google.com', dateEntered=datetime.date(2021, 1, 1), posterUser=self.posteruser, resourceDescription="lorem ipsum")

    def test_string(self):
        self.assertEqual(str(self.resource), "ResourceA")  

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.posteruser=User(username='user1')
        self.event=Event(eventTitle="EventA", eventLocation="LocationA",eventDate=datetime.date(2021, 1, 1), eventTime=datetime.time(12,0,0,0), eventDescription="lorem ipsum", posterUser=self.posteruser)

    def test_string(self):
        self.assertEqual(str(self.event), "EventA")  

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')