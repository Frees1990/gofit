# Generated by Django 3.2.25 on 2024-11-27 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_usermembership'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
