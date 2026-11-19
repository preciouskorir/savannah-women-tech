# Generated for the programme application model.
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProgrammeApplication",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=30)),
                ("country", models.CharField(max_length=100)),
                ("programme", models.CharField(choices=[
                    ("digital_skills", "Digital Skills Academy"),
                    ("ai_ml", "AI & Machine Learning"),
                    ("leadership", "Leadership & Mentorship"),
                    ("entrepreneurship", "Entrepreneurship Hub"),
                    ("scholarships", "Scholarships & Grants"),
                    ("mentorship", "Mentorship Network"),
                    ("community", "Community Outreach"),
                ], max_length=40)),
                ("background", models.TextField(blank=True, help_text="Tell us about your education, work or relevant experience.")),
                ("motivation", models.TextField(help_text="Why are you interested in this programme?")),
                ("consent", models.BooleanField(default=False, verbose_name="I agree that Savannah Women Tech may use these details to review my programme application and contact me about it.")),
                ("status", models.CharField(choices=[
                    ("pending", "Pending"),
                    ("shortlisted", "Shortlisted"),
                    ("accepted", "Accepted"),
                    ("declined", "Declined"),
                ], default="pending", max_length=12)),
                ("admin_notes", models.TextField(blank=True)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("reviewed_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "programme application",
                "verbose_name_plural": "programme applications",
                "ordering": ["-submitted_at"],
            },
        ),
    ]
