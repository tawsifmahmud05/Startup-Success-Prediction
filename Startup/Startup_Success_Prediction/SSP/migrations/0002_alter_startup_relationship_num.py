# Generated by Django 3.2.6 on 2022-02-22 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='relationship_num',
            field=models.PositiveIntegerField(max_length=100),
        ),
    ]
