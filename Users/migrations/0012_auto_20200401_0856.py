# Generated by Django 3.0.2 on 2020-04-01 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_reply_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='addqueryuser_tb',
            name='status_file',
            field=models.CharField(default='Valid', max_length=20),
        ),
        migrations.AddField(
            model_name='addqueryuser_tb',
            name='status_post',
            field=models.CharField(default='Valid', max_length=20),
        ),
        migrations.AlterField(
            model_name='addqueryuser_tb',
            name='addquery',
            field=models.CharField(default='spam', max_length=220),
        ),
        migrations.AlterField(
            model_name='addqueryuser_tb',
            name='subject',
            field=models.CharField(default='spam', max_length=30),
        ),
    ]
