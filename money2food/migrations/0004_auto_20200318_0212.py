# Generated by Django 3.0.4 on 2020-03-18 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money2food', '0003_auto_20200318_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='measure_unit',
            field=models.CharField(choices=[('g', 'grams'), ('ml', 'milliliter'), ('pcs', 'pieces')], max_length=10),
        ),
    ]
