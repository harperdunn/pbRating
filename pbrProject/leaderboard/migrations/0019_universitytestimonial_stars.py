# Generated by Django 4.2.19 on 2025-03-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0018_universitytestimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='universitytestimonial',
            name='stars',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
