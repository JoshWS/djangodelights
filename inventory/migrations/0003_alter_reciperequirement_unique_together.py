# Generated by Django 5.0.3 on 2024-03-15 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_purchase_timestamp'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reciperequirement',
            unique_together=set(),
        ),
    ]