from django import forms

from .models import MembershipApplication, ProgrammeApplication


class MembershipApplicationForm(forms.ModelForm):
    class Meta:
        model = MembershipApplication
        fields = [
            "full_name",
            "email",
            "phone",
            "country",
            "interests",
            "reason",
            "consent",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"autocomplete": "name", "placeholder": "Your full name"}),
            "email": forms.EmailInput(attrs={"autocomplete": "email", "placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"autocomplete": "tel", "placeholder": "Include country code if possible"}),
            "country": forms.TextInput(attrs={"autocomplete": "country-name", "placeholder": "Your country"}),
            "interests": forms.Textarea(attrs={"rows": 3, "placeholder": "What would you like to learn or contribute to?"}),
            "reason": forms.Textarea(attrs={"rows": 4, "placeholder": "Tell us briefly why you would like to become a member."}),
        }

    def clean_email(self):
        return self.cleaned_data["email"].strip().lower()

    def clean_consent(self):
        if not self.cleaned_data.get("consent"):
            raise forms.ValidationError("Please confirm your consent before submitting.")
        return True


class ProgrammeApplicationForm(forms.ModelForm):
    class Meta:
        model = ProgrammeApplication
        fields = [
            "full_name",
            "email",
            "phone",
            "country",
            "programme",
            "background",
            "motivation",
            "consent",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "autocomplete": "name",
                "placeholder": "Your full name",
            }),
            "email": forms.EmailInput(attrs={
                "autocomplete": "email",
                "placeholder": "you@example.com",
            }),
            "phone": forms.TextInput(attrs={
                "autocomplete": "tel",
                "placeholder": "Include country code if possible",
            }),
            "country": forms.TextInput(attrs={
                "autocomplete": "country-name",
                "placeholder": "Your country",
            }),
            "programme": forms.Select(),
            "background": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Tell us about your education, work or relevant experience (optional).",
            }),
            "motivation": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Why are you interested in this programme, and what do you hope to gain?",
            }),
        }

    def clean_email(self):
        return self.cleaned_data["email"].strip().lower()

    def clean_consent(self):
        if not self.cleaned_data.get("consent"):
            raise forms.ValidationError(
                "Please confirm your consent before submitting."
            )
        return True
