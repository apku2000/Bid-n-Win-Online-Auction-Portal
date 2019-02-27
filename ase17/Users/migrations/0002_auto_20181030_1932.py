# Generated by Django 2.1.2 on 2018-10-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='display_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='card_no',
            field=models.CharField(max_length=16),
        ),
    ]
