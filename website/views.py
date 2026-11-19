from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import MembershipApplicationForm, ProgrammeApplicationForm
from .models import ProgrammeApplication


def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


def programs(request):
    return render(request, 'website/programs.html')


def events(request):
    return render(request, 'website/events.html')


def blog(request):
    return render(request, 'website/blog.html')


def gallery(request):
    return render(request, 'website/gallery.html')


def volunteer(request):
    return render(request, 'website/volunteer.html')


def contact(request):
    return render(request, 'website/contact.html')


def donate(request):
    return render(request, 'website/donate.html')


def membership(request):
    if request.method == "POST":
        form = MembershipApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for applying to join Savannah Women Tech. Your application has been received and is awaiting review.",
            )
            return redirect("membership")
    else:
        form = MembershipApplicationForm()

    return render(request, "website/membership.html", {"form": form})


def programme_application(request):
    valid_programmes = {choice[0] for choice in ProgrammeApplication.Programme.choices}

    if request.method == "POST":
        form = ProgrammeApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for applying. Savannah Women Tech has received your programme application. Our team will review it and contact you about the outcome.",
            )
            return redirect("programme_application")
    else:
        selected_programme = request.GET.get("programme", "")
        initial = (
            {"programme": selected_programme}
            if selected_programme in valid_programmes
            else {}
        )
        form = ProgrammeApplicationForm(initial=initial)

    return render(
        request,
        "website/programme_application.html",
        {"form": form},
    )
