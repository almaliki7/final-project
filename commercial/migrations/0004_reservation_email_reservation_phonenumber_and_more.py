# Generated by Django 4.2.5 on 2023-09-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0003_coffeebreak_picture_alter_specialoffer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='phoneNumber',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='UserReservationHistory',
        ),
    ]
