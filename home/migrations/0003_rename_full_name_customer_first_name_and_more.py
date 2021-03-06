# Generated by Django 4.0.3 on 2022-03-30 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
