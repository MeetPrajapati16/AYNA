# Generated by Django 5.1.2 on 2025-03-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_data_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
