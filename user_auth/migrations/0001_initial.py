# Generated by Django 3.1 on 2021-06-21 20:03
from django.conf import settings
from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    for g_name in settings.STAFF_GROUPS:
        g, _ = Group.objects.get_or_create(name=g_name)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_groups, reverse_code=migrations.RunPython.noop),
    ]
