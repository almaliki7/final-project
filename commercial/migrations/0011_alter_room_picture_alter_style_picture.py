# Generated by Django 4.2.5 on 2023-10-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0010_rename_firstname_reservation_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='picture',
            field=models.ImageField(null=True, upload_to='media/room/'),
        ),
        migrations.AlterField(
            model_name='style',
            name='picture',
            field=models.ImageField(null=True, upload_to='media/style/'),
        ),
    ]