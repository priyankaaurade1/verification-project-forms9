# Generated by Django 3.2.7 on 2023-04-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0025_auto_20230404_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentupload',
            old_name='client_id',
            new_name='client_id_1',
        ),
        migrations.AddField(
            model_name='documentupload',
            name='client_id_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='documentupload',
            name='client_id_3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='documentupload',
            name='client_id_4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
