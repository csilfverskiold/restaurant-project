# Generated by Django 3.2.16 on 2023-01-31 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_remove_reservation_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='title',
            field=models.CharField(default='Reservation: Dinner', max_length=200),
        ),
    ]
