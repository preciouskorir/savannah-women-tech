from django.db import models


class MembershipApplication(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        DECLINED = "declined", "Declined"

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=100)
    interests = models.TextField(help_text="Tell us which areas interest you, such as digital skills, AI, mentorship, leadership or entrepreneurship.")
    reason = models.TextField(verbose_name="Why would you like to join Savannah Women Tech?")
    consent = models.BooleanField(
        default=False,
        verbose_name="I agree that Savannah Women Tech may use these details to review my membership application and contact me about it.",
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "membership application"
        verbose_name_plural = "membership applications"

    def __str__(self):
        return f"{self.full_name} ({self.get_status_display()})"


class ProgrammeApplication(models.Model):
    class Programme(models.TextChoices):
        DIGITAL_SKILLS = "digital_skills", "Digital Skills Academy"
        AI_ML = "ai_ml", "AI & Machine Learning"
        LEADERSHIP = "leadership", "Leadership & Mentorship"
        ENTREPRENEURSHIP = "entrepreneurship", "Entrepreneurship Hub"
        SCHOLARSHIPS = "scholarships", "Scholarships & Grants"
        MENTORSHIP = "mentorship", "Mentorship Network"
        COMMUNITY = "community", "Community Outreach"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        SHORTLISTED = "shortlisted", "Shortlisted"
        ACCEPTED = "accepted", "Accepted"
        DECLINED = "declined", "Declined"

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=100)
    programme = models.CharField(max_length=40, choices=Programme.choices)
    background = models.TextField(
        blank=True,
        help_text="Tell us about your education, work or relevant experience.",
    )
    motivation = models.TextField(
        help_text="Why are you interested in this programme?",
    )
    consent = models.BooleanField(
        default=False,
        verbose_name="I agree that Savannah Women Tech may use these details to review my programme application and contact me about it.",
    )
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.PENDING,
    )
    admin_notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "programme application"
        verbose_name_plural = "programme applications"

    def __str__(self):
        return f"{self.full_name} - {self.get_programme_display()}"
