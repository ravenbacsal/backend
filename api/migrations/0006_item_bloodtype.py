# Generated by Django 5.0.6 on 2024-07-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_birthdate_item_civil_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bloodtype',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
