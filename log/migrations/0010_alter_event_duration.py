# Generated by Django 4.2.5 on 2023-09-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0009_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.DurationField(),
        ),
    ]