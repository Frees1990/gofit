# Generated by Django 3.2.25 on 2025-03-07 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_delete_membershiporder'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
