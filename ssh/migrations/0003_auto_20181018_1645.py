# Generated by Django 2.0.5 on 2018-10-18 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssh', '0002_auto_20181018_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ssh',
            name='ip_address',
            field=models.GenericIPAddressField(unique=True),
        ),
    ]
