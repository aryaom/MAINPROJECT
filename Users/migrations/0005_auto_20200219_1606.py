# Generated by Django 3.0.3 on 2020-02-20 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20200219_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='userregistration_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='hh', max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('pincode', models.CharField(default='nothing', max_length=20)),
                ('mailid', models.CharField(max_length=20)),
                ('phonenum', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
                ('experience', models.CharField(default='nothing', max_length=20)),
                ('designation', models.CharField(default='nothing', max_length=20)),
                ('companyname', models.CharField(default='nothing', max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='userregistration',
        ),
    ]