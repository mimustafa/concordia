# Generated by Django 2.2 on 2019-05-03 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("concordia", "0029_assettranscriptionreservation_reservation_token")
    ]

    operations = [
        migrations.RemoveField(model_name="assettranscriptionreservation", name="user"),
        migrations.AlterField(
            model_name="assettranscriptionreservation",
            name="reservation_token",
            field=models.CharField(max_length=50),
        ),
    ]
