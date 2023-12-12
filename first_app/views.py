from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import models, forms


# Create your views here.

def index(request):
    test_dict = {'text': 'hello world', 'number': 100}
    webpages_ls = models.AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_ls}

    # Merge the two dictionaries
    context_dict = {**test_dict, **date_dict}
    return render(request, 'first_app/index.html', context=context_dict)


def help_page(request):
    my_dict = {'help_insert': '... thats too bad :('}
    return render(request, 'first_app/help.html', context=my_dict)


def users_page(request):
    users_ls = models.Users.objects.order_by('last_name')
    user_dict = {'users': users_ls}
    return render(request, 'first_app/users.html', context=user_dict)


def form_page(request):
    form = forms.NewUserForm()

    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users_page(request)
        else:
            print('ERROR: Form is invalid!')

    return render(request, 'first_app/form.html', context={'form': form})


def other_page(request):
    return render(request, 'first_app/other.html')


def relative_page(request):
    return render(request, 'first_app/relative_url_templates.html')


def register_page(request):
    registered = False
    if request.method == 'POST':
        user_form = forms.NewUserProfileForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES.get('profile_pic')

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.NewUserProfileForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'first_app/registration.html', context={'user_form': user_form,
                                                                   'profile_form': profile_form,
                                                                   'registered': registered})


def user_login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Unsuccessful login attempt!')
            print(f'Username: {username} and password: {password}')
            return HttpResponse('Invalid Login Details!')
    else:
        return render(request, 'first_app/login.html', {})


@login_required
def user_logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special_page(request):
    return HttpResponse('You are logged in! :D')
