# Generated by Django 3.0.3 on 2020-02-13 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SiteAdmin', '0003_groupadminregistration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='groupadminregistration',
            new_name='groupadmins',
        ),
    ]
