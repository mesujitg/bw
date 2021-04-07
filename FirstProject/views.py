from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from FirstProject.forms import UserRegistrationForm
from FirstProject.settings import MEDIA_URL
from about.models import About
from counter.models import Counter
from counts.models import Count
from courses.models import Course, Type
from subscribers.models import Subscriber


def show_home(request):
    intro = About.objects.filter(title='Introduction')
    counts = Count.objects.get(id=1)
    counters = Counter.objects.all()
    courses = Course.objects.all()
    types = Type.objects.all()
    return render(request, 'index.html', {'intro': intro[0], 'counts': counts, 'counters': counters,
                                          'types': types, 'courses': courses, 'MEDIA_URL': MEDIA_URL})


def show_portfolio(request):
    return render(request, 'portfolio.html')


def do_subscribe(request):
    email = request.POST['email']

    subscriber = Subscriber(email=email)
    subscriber.save()
    return redirect('/')


def do_login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            # request.session['username'] = un
            messages.success(request, 'You are logged in !!!')
            return redirect('home')
        else:
            messages.warning(request, 'Wrong Credentials')
            return redirect('login')

    return render(request, 'login.html')


def do_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        form.save()
        # fn = request.POST['fn']
        # ln = request.POST['ln']
        # em = request.POST['em']
        # un = request.POST['un']
        # pw = request.POST['pw']
        #
        # user = User(first_name=fn, last_name=ln, email=em, username=un, password=pw)
        # user.save()
        messages.success(request, 'Registered Successfully !')
        return redirect('login')

    # form = UserRegistrationForm()
    form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def do_logout(request):
    auth.logout(request)
    return redirect('home')
