# Generated by Django 3.1.4 on 2020-12-15 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0009_auto_20201215_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='Track_name',
        ),
    ]
