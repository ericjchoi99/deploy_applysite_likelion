# Generated by Django 3.0.8 on 2020-08-04 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0007_auto_20200805_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyinformation',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
