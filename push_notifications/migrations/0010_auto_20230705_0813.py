# Generated by Django 3.2.17 on 2023-07-05 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0009_alter_apnsdevice_device_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='apnsdevice',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Update date'),
        ),
        migrations.AddField(
            model_name='gcmdevice',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Update date'),
        ),
        migrations.AddField(
            model_name='webpushdevice',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Update date'),
        ),
        migrations.AddField(
            model_name='wnsdevice',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Update date'),
        ),
    ]
