from django.shortcuts import render


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