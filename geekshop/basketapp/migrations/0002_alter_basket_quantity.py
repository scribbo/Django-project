# Generated by Django 3.2.11 on 2022-05-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
