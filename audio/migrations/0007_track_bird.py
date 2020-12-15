# Generated by Django 3.1.4 on 2020-12-15 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birdlist', '0005_auto_20201215_2246'),
        ('audio', '0006_remove_track_uploaded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='bird',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='birdlist.birdlistings'),
        ),
    ]
