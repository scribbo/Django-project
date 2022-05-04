# Generated by Django 3.2.11 on 2022-05-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='shopuser',
            name='avatar',
        ),
        migrations.AddField(
            model_name='shopuser',
            name='city',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
