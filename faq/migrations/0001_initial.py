# Generated by Django 2.0.4 on 2018-04-26 08:52

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="FAQ",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question",
                    models.TextField(
                        help_text="The actual question itself.", verbose_name="question"
                    ),
                ),
                (
                    "answer",
                    models.TextField(
                        blank=True, help_text="The answer text.", verbose_name="answer"
                    ),
                ),
                ("slug", models.SlugField(max_length=100, verbose_name="slug")),
                (
                    "created_on",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="created on"
                    ),
                ),
                ("updated_on", models.DateTimeField(verbose_name="updated on")),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="created by",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="updated by",
                    ),
                ),
            ],
        )
    ]
