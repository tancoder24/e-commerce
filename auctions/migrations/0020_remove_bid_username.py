# Generated by Django 3.1.7 on 2021-05-26 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20210527_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='username',
        ),
    ]