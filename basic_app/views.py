# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from basic_app.forms import UserProfileInfoForm, UserForm


# Create your views here.


# make the index page
def index(request):


    return render(request, 'index.html')


@logout_required
@login_required
def special(request):
    return HttpResponse('You are logged in')


def user_login(request):
    return render(request, 'login.html')


# make the registration view
def register(request):
    registered = False
    if request.method == 'POST':
        # get info from both forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # check if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # save htme to the DB
            user = user_form.save()
            # Hash Password
            user.set_password(user.password)
            # save again
            user.save()

            # deal with profile info form
            profile = profile_form.save(commit=False)
            # sets one to one relationship between User Form and User PIF
            profile.user = user
            # manipulation
            if 'picture' in request.FILES:
                print('FOUND A PROFILE PICTURE SUBMITTED')
                # FILES contains a dictionary of the media dirs
                profile.picture = request.FILES['profile_pictures']

            # same tactic when dealing with files
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    # if it wasn't an http post, render the forms as blanks so that her cna do it Hin
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
