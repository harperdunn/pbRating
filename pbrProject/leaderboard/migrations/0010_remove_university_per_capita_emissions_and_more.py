# Generated by Django 5.1.5 on 2025-02-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0009_university_rename_universities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='per_capita_emissions',
        ),
        migrations.RemoveField(
            model_name='university',
            name='plant_dairy_options',
        ),
        migrations.RemoveField(
            model_name='university',
            name='reduction_animal_based_1yr',
        ),
        migrations.RemoveField(
            model_name='university',
            name='reduction_animal_based_5yr',
        ),
        migrations.RemoveField(
            model_name='university',
            name='vegan_station',
        ),
        migrations.AddField(
            model_name='university',
            name='overallGrade',
            field=models.CharField(default='F', max_length=255),
        ),
        migrations.AddField(
            model_name='university',
            name='plant_breakfast_options',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='animal_based_percentage',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='culinary_training',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='default_veg_program',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='formal_commitments',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='labeling',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='meatless_monday',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='naming',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='overallScore',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='university',
            name='plant_desserts',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='salad_protein',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='student_satisfaction',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='vegan_meals',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
