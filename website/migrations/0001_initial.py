# Generated for the first membership application model.
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MembershipApplication",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=30)),
                ("country", models.CharField(max_length=100)),
                ("interests", models.TextField(help_text="Tell us which areas interest you, such as digital skills, AI, mentorship, leadership or entrepreneurship.")),
                ("reason", models.TextField(verbose_name="Why would you like to join Savannah Women Tech?")),
                ("consent", models.BooleanField(default=False, verbose_name="I agree that Savannah Women Tech may use these details to review my membership application and contact me about it.")),
                ("status", models.CharField(choices=[("pending", "Pending"), ("approved", "Approved"), ("declined", "Declined")], default="pending", max_length=10)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("reviewed_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "membership application",
                "verbose_name_plural": "membership applications",
                "ordering": ["-submitted_at"],
            },
        ),
    ]
