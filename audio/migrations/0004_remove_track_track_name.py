# Generated by Django 3.1.4 on 2020-12-15 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_auto_20201215_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='Track_name',
        ),
    ]