# Generated by Django 3.2.7 on 2023-04-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0022_alter_investordetail_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentupload',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
