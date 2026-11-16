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
