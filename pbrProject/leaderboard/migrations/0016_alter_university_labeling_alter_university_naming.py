# Generated by Django 4.2.19 on 2025-02-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0015_alter_university_formal_commitments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='labeling',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='naming',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
