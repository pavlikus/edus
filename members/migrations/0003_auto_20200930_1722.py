# Generated by Django 3.1.1 on 2020-09-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20200930_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='position',
            field=models.CharField(max_length=64),
        ),
    ]
