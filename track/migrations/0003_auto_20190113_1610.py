# Generated by Django 2.0 on 2019-01-13 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20190113_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image_vehicle',
            old_name='vehicle_no',
            new_name='vehicle_number',
        ),
    ]
