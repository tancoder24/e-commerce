# Generated by Django 3.1.7 on 2021-05-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_bid_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='imagelink',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]
