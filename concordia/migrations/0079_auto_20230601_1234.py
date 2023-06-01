# Generated by Django 3.2.18 on 2023-06-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("concordia", "0078_alter_sitereport_report_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofileactivity",
            name="asset_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="userprofileactivity",
            name="asset_tag_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="userprofileactivity",
            name="review_count",
            field=models.IntegerField(
                default=0, verbose_name="transcription review count"
            ),
        ),
        migrations.AlterField(
            model_name="userprofileactivity",
            name="transcribe_count",
            field=models.IntegerField(
                default=0, verbose_name="transcription save/submit count"
            ),
        ),
    ]