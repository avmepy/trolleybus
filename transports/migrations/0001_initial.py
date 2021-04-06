# Generated by Django 3.1.7 on 2021-04-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Короткий опис')),
                ('description', models.TextField(blank=True, verbose_name='Детальний опис')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_plate', models.CharField(max_length=10, verbose_name='Автомобільний номер')),
                ('condition', models.CharField(blank=True, default='ok', max_length=1000, verbose_name='Стан')),
                ('mileage', models.IntegerField(blank=True, verbose_name='Пробіг (тис. км)')),
            ],
        ),
    ]
