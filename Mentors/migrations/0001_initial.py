# Generated by Django 3.0.3 on 2020-02-25 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GroupAdmin', '0002_queryallocation'),
        ('Users', '0008_auto_20200224_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='reply_mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=20)),
                ('fileupload', models.FileField(upload_to='')),
                ('date', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('mentor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GroupAdmin.mentorsregistration')),
                ('query_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.addqueryUSER_tb')),
            ],
        ),
    ]