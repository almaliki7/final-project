# Generated by Django 4.2.5 on 2023-09-30 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0007_rename_pricing_per_hour_room_rate_per_hour_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='event_space',
            new_name='event_space_1',
        ),
    ]
