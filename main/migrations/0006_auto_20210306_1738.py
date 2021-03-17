# Generated by Django 3.1.7 on 2021-03-06 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_route_stop_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='schedule',
        ),
        migrations.AddField(
            model_name='route',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='route',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='main.route'),
        ),
    ]
