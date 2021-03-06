# Generated by Django 3.1.7 on 2021-05-26 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20210526_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bids_listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='relate_bid', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='auction_Listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='relate_comments', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('Fashion', 'Fashion'), ('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Books', 'Books')], default='All', max_length=100),
        ),
    ]
