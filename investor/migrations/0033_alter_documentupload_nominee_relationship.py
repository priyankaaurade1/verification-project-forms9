# Generated by Django 3.2.7 on 2023-04-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0032_auto_20230407_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentupload',
            name='nominee_relationship',
            field=models.CharField(blank=True, choices=[('MOTHER', 'MOTHER'), ('FATHER', 'FATHER'), ('SISTER', 'SISTER'), ('BROTHER', 'BROTHER'), ('SON', 'SON'), ('DAUGHTER', 'DAUGHTER'), ('OTHER', 'OTHER')], max_length=20, null=True),
        ),
    ]
