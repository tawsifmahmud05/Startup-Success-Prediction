# Generated by Django 3.2.6 on 2022-02-22 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSP', '0002_alter_startup_relationship_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='funding_round_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='startup',
            name='milestones_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='startup',
            name='relationship_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
