# Generated by Django 3.2.6 on 2022-02-22 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SSP', '0003_auto_20220223_0317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startup',
            old_name='milestones_num',
            new_name='milestone_num',
        ),
    ]
