# Generated by Django 4.1.7 on 2023-07-14 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habrieapp", "0004_alter_academicdetail_session_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="document",
            name="document",
        ),
        migrations.AlterField(
            model_name="document",
            name="document_name",
            field=models.FileField(default=1, upload_to="documents"),
            preserve_default=False,
        ),
    ]
