from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


# Create your views here.
def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main_page'))
    else:
        login_form = AuthenticationForm()
    context = {
        'title': 'Вход',
        'login_form': login_form
    }
    return render(request, 'pages/login.tpl', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main_page'))
