# Generated by Django 3.1.4 on 2020-12-15 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birdlist', '0006_auto_20201215_2305'),
        ('birdinfo', '0002_auto_20201214_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='birdinfo',
            name='bird',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='birdlist.birdlistings'),
        ),
    ]
