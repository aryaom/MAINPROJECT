# Generated by Django 2.2.1 on 2013-11-06 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_queryallocation_reply_mentor_usercomplaints_tb'),
    ]

    operations = [
        migrations.DeleteModel(
            name='reply_mentor',
        ),
    ]
