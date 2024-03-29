# Generated by Django 3.1.3 on 2022-06-13 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_repairpart_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairPartRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('is_completed', models.BooleanField(default=False)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.repairpart')),
            ],
        ),
    ]
