# Generated by Django 4.2 on 2023-10-27 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useradmin',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='admin_user', to='authentication.user'),
        ),
    ]
