# Generated by Django 4.0.3 on 2022-05-01 21:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Club', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MeetingMinutes',
            new_name='MeetingMinute',
        ),
        migrations.AlterModelOptions(
            name='meetingminute',
            options={'verbose_name_plural': 'meetingMinutes'},
        ),
        migrations.AlterModelTable(
            name='meetingminute',
            table='meetingMinute',
        ),
    ]