# Generated by Django 3.2.5 on 2021-08-21 03:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0003_auto_20210820_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='answer',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]