# Generated by Django 3.1.2 on 2020-10-04 15:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planId', models.IntegerField()),
                ('name', models.TextField()),
                ('startTime', models.IntegerField()),
                ('endTime', models.IntegerField()),
                ('progressTime', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
