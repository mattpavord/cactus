# Generated by Django 3.0.8 on 2020-09-24 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raincheck', '0003_change_region_fiel_dn_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='plants',
        ),
        migrations.CreateModel(
            name='CustomerPlant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raincheck.Customer')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raincheck.Plant')),
            ],
        ),
    ]