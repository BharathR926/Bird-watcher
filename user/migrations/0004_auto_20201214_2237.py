# Generated by Django 3.1.4 on 2020-12-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201214_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
