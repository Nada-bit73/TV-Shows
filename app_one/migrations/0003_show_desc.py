# Generated by Django 2.2.4 on 2022-06-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_auto_20220619_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='desc',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
