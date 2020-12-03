# Generated by Django 3.0.8 on 2020-12-03 17:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raincheck', '0007_auto_20201120_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='customerplant',
            unique_together={('plant_id', 'customer_id')},
        ),
    ]
