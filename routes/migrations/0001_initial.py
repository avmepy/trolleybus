# Generated by Django 3.1.7 on 2021-04-06 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Назва маршруту')),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва зупинки')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='Адреса')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledStop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Час зупинки')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='routes.stop')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cruise_number', models.IntegerField(verbose_name='Номер рейсу')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.route')),
                ('scheduled_stops', models.ManyToManyField(to='routes.ScheduledStop')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='stops',
            field=models.ManyToManyField(to='routes.Stop'),
        ),
    ]
