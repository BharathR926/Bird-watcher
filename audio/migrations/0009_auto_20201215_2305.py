# Generated by Django 3.1.4 on 2020-12-15 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birdlist', '0006_auto_20201215_2305'),
        ('audio', '0008_auto_20201215_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='bird',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='birdlist.birdlistings'),
        ),
    ]
