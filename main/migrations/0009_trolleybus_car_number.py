# Generated by Django 3.1.7 on 2021-03-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_trolleybus_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='trolleybus',
            name='car_number',
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
    ]
