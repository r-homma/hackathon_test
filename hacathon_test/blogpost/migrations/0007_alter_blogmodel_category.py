# Generated by Django 3.2.5 on 2021-08-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0006_blogmodel_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='category',
            field=models.CharField(choices=[('network', 'ネットワーク'), ('linux', 'lunux'), ('other', 'その他')], max_length=50),
        ),
    ]
