# Generated by Django 3.2.16 on 2023-02-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_remove_reservation_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(choices=[('5 PM', '5 PM'), ('5:30 PM', '5:30 PM'), ('6 PM', '6 PM'), ('6:30 PM', '6:30 PM'), ('7 PM', '7 PM'), ('7:30 PM', '7:30 PM'), ('8 PM', '8 PM'), ('8:30 PM', '8:30 PM'), ('9 PM', '9 PM'), ('9:30 PM', '9:30 PM')], max_length=10),
        ),
    ]
