# Generated by Django 3.2.6 on 2022-04-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSP', '0007_auto_20220420_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='avg_participants',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
