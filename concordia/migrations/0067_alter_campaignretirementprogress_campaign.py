# Generated by Django 3.2.16 on 2023-02-22 20:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("concordia", "0066_campaignretirementprogress"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaignretirementprogress",
            name="campaign",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="concordia.campaign"
            ),
        ),
    ]
