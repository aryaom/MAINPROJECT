# Generated by Django 3.0.3 on 2020-02-18 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='groupadmins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('mailid', models.CharField(max_length=20)),
                ('phonenum', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
