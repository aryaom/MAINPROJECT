# Generated by Django 3.0.3 on 2020-02-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteAdmin', '0002_addgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='groupadminregistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('mailid', models.CharField(max_length=20)),
                ('phonenum', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
                ('experience', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('group', models.CharField(max_length=20)),
            ],
        ),
    ]