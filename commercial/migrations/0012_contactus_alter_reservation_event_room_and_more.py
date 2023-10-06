# Generated by Django 4.2.5 on 2023-10-06 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0011_alter_room_picture_alter_style_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('subject', models.CharField(max_length=255, null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='event_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commercial.room'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='event_style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commercial.style'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='picture',
            field=models.ImageField(null=True, upload_to='rooms/'),
        ),
        migrations.AlterField(
            model_name='style',
            name='picture',
            field=models.ImageField(null=True, upload_to='styles/'),
        ),
    ]
