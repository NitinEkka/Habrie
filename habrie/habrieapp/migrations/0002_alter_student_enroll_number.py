# Generated by Django 4.1.7 on 2023-07-14 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("habrieapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="enroll_number",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="habrieapp.academicdetail",
            ),
        ),
    ]