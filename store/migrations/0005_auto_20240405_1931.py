# Generated by Django 3.1 on 2024-04-05 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20240405_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='created_at',
            new_name='created_date',
        ),
    ]