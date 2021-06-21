# Generated by Django 3.1 on 2021-06-21 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='distance',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_number', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('amount_entries', models.PositiveIntegerField(default=0)),
                ('total_duration', models.PositiveIntegerField(default=0)),
                ('total_distance', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistic', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='statistic_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entries.statistic'),
        ),
    ]
