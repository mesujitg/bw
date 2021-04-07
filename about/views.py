from django.http import HttpResponse
from django.shortcuts import render
from FirstProject.settings import MEDIA_URL
from about.models import About


def show_about(request):
    about = About.objects.all()
    return render(request, 'about.html', {'about': about, 'MEDIA_URL': MEDIA_URL})
