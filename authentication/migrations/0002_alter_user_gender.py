# Generated by Django 4.2 on 2023-10-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')], default=2),
        ),
    ]
