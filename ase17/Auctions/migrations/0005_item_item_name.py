# Generated by Django 2.1.2 on 2018-11-03 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auctions', '0004_auctionbidders'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]