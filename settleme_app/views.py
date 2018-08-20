from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from settleme_app.forms import UserForm

# Create your views here.


def index(request):
    return render(request, 'settleme_app/index.html')


@login_required
def main_menu(request):
    return render(request, 'settleme_app/menu.html')


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main_menu'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to log in and failed")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("invalid login details")
    else:
        return render(request, 'settleme_app/login.html')


def signup(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            return HttpResponse(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'settleme_app/signup.html',
                  {'user_form': user_form,
                   'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

