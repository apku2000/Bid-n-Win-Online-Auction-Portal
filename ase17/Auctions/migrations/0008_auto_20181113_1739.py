# Generated by Django 2.1.3 on 2018-11-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auctions', '0007_auto_20181113_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('1', 'Electronics'), ('2', 'Automobiles'), ('3', 'Fashion'), ('4', 'Sports'), ('5', 'Art'), ('6', 'Books'), ('7', 'Furniture'), ('8', 'Antiques'), ('9', 'Musical Equipment'), ('10', 'Industrial Equipment'), ('11', 'Gaming'), ('12', 'Stationary'), ('13', 'Industrial Equipment'), ('14', 'Precious Gems'), ('15', 'Pet Stuff'), ('16', 'Miscellaneous')], max_length=200),
        ),
    ]