# Generated by Django 3.1.7 on 2021-04-06 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transports', '0005_remove_transport_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='condition',
            field=models.CharField(blank=True, default='ok', max_length=1000, verbose_name='Стан'),
        ),
    ]
