# Generated by Django 3.2.18 on 2023-05-04 15:33

from django.db import migrations, models


def update_report_names(apps, schema_editor):
    SiteReport = apps.get_model("concordia", "SiteReport")
    for report in SiteReport.objects.filter(report_name="RETIRED TOTAL"):
        report.report_name = "RETIRED_TOTAL"
        report.save()
    for report in SiteReport.objects.filter(report_name="Retired campaigns"):
        report.report_name = "RETIRED_TOTAL"
        report.save()
    for report in SiteReport.objects.filter(
        report_name="Active and completed campaigns"
    ):
        report.report_name = "TOTAL"
        report.save()
    for report in SiteReport.objects.filter(
        report_name="", campaign__isnull=True, topic__isnull=True
    ):
        report.report_name = "TOTAL"
        report.save()


def backwards(apps, schema_editor):
    # This can't be reversed, so we leave the report_names alone
    return


class Migration(migrations.Migration):
    dependencies = [
        ("concordia", "0076_sitereport_report_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sitereport",
            name="report_name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("TOTAL", "Active and completed campaigns"),
                    ("RETIRED_TOTAL", "Retired campaigns"),
                ],
                default="",
                max_length=20,
            ),
        ),
        migrations.RunPython(update_report_names, backwards),
    ]
