# Generated by Django 2.2.10 on 2020-02-25 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0039_auto_20200221_0257"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="serviceaccount",
            options={
                "ordering": ("name", "pk"),
                "permissions": (("manage_service_accounts", "Manage service account"),),
            },
        ),
        migrations.AlterModelOptions(
            name="staffnotificationrecipient", options={"ordering": ("staff_email",)},
        ),
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ("email",),
                "permissions": (
                    ("manage_users", "Manage customers."),
                    ("manage_staff", "Manage staff."),
                ),
            },
        ),
    ]
