# Generated by Django 3.1.7 on 2021-03-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataAnalysis', '0002_auto_20210311_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
