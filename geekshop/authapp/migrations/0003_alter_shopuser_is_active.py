# Generated by Django 3.2.11 on 2022-06-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_alter_shopuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]