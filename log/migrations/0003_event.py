# Generated by Django 4.2.5 on 2023-09-11 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_register_varieties_delete_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=20)),
                ('instruction', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('registration_fee', models.IntegerField()),
                ('contact_number', models.BigIntegerField()),
                ('duration', models.TimeField()),
                ('venue', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.varieties')),
            ],
        ),
    ]