# Generated by Django 3.2.7 on 2023-03-21 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20230226_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usertyperole'),
        ),
    ]
