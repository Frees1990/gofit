# Generated by Django 3.2.25 on 2024-11-28 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_membership_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='duration',
            field=models.PositiveIntegerField(help_text='Duration in months'),
        ),
    ]
