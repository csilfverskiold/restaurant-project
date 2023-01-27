# Generated by Django 3.2.16 on 2023-01-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20230127_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='Email Address', max_length=100),
        ),
        migrations.AddField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(default='First Name', max_length=100),
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(default='Last Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='guest',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(choices=[('3 PM', '3 PM'), ('3:30 PM', '3:30 PM'), ('4 PM', '4 PM'), ('4:30 PM', '4:30 PM'), ('5 PM', '5 PM'), ('5:30 PM', '5:30 PM'), ('6 PM', '6 PM'), ('6:30 PM', '6:30 PM'), ('7 PM', '7 PM'), ('7:30 PM', '7:30 PM')], max_length=10),
        ),
    ]
