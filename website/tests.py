from django.test import TestCase
from django.urls import reverse

from .models import ProgrammeApplication


class ProgrammeApplicationTests(TestCase):
    def setUp(self):
        self.application_url = reverse("programme_application")
        self.valid_data = {
            "full_name": "Amina Test",
            "email": "AMINA@example.com",
            "phone": "+254700000000",
            "country": "Kenya",
            "programme": ProgrammeApplication.Programme.DIGITAL_SKILLS,
            "background": "Recent graduate interested in web development.",
            "motivation": "I want to build practical digital skills.",
            "consent": "on",
        }

    def test_application_page_loads(self):
        response = self.client.get(self.application_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "website/programme_application.html")

    def test_programme_is_prefilled_from_apply_link(self):
        response = self.client.get(
            self.application_url,
            {"programme": ProgrammeApplication.Programme.AI_ML},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["form"]["programme"].value(),
            ProgrammeApplication.Programme.AI_ML,
        )

    def test_valid_application_is_saved(self):
        response = self.client.post(self.application_url, self.valid_data)
        self.assertRedirects(response, self.application_url)
        self.assertEqual(ProgrammeApplication.objects.count(), 1)

        application = ProgrammeApplication.objects.get()
        self.assertEqual(application.full_name, "Amina Test")
        self.assertEqual(application.email, "amina@example.com")
        self.assertEqual(
            application.programme,
            ProgrammeApplication.Programme.DIGITAL_SKILLS,
        )
        self.assertEqual(application.status, ProgrammeApplication.Status.PENDING)

    def test_application_without_consent_is_not_saved(self):
        invalid_data = self.valid_data.copy()
        invalid_data["consent"] = ""
        response = self.client.post(self.application_url, invalid_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ProgrammeApplication.objects.count(), 0)
        self.assertIn("consent", response.context["form"].errors)
