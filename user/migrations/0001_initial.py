# Generated by Django 3.1.4 on 2020-12-14 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('country', models.CharField(max_length=50)),
                ('is_verified', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
