# Generated by Django 3.1.3 on 2022-06-13 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_repairtask'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repairpart',
            name='category',
        ),
        migrations.DeleteModel(
            name='PartCategory',
        ),
    ]
