# Generated by Django 2.0.1 on 2018-01-27 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]