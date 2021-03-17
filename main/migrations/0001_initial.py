# Generated by Django 3.1.7 on 2021-03-04 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StopPoint',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trolleybus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(blank=True, null=True)),
                ('last_maintenance_date', models.DateField(blank=True, null=True)),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.state')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.TimeField(blank=True, null=True)),
                ('stop_point', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.stoppoint')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.schedule')),
                ('stop_points', models.ManyToManyField(to='main.StopPoint')),
            ],
        ),
    ]