# Generated by Django 2.2.1 on 2013-11-06 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GroupAdmin', '0003_delete_queryallocation'),
        ('Users', '0010_delete_reply_mentor'),
    ]

    operations = [
        migrations.CreateModel(
            name='reply_mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=20)),
                ('fileupload', models.FileField(upload_to='')),
                ('date', models.CharField(max_length=20)),
                ('status_post', models.CharField(max_length=20)),
                ('status_file', models.CharField(max_length=20)),
                ('mentor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GroupAdmin.mentorsregistration')),
                ('query_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.addqueryUSER_tb')),
            ],
        ),
    ]
