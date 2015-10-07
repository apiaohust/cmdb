# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from cmdb.forms import UserForm, UserProfileForm


def register(request):
    registered = False
    result = {}
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            tempusername = user.username
            temppassword =user.password
            profile = profile_form.save()
            if profile.permission == 'admin':
               user.user_permissions.add(41)
            user.set_password(user.password)
            user.save()
            usertemp = authenticate(username=tempusername, password=temppassword)
            login(request,usertemp)
            registered = True
        else:
            print user_form.errors,
            return HttpResponse(user_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        result = {'user_form': user_form,'profile_form':profile_form,  'registered': registered}
    if registered:
        return HttpResponseRedirect('/cmdb/')
    else:
        return render(request, 'cmdb/register.html', result)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print request.user.has_perm('cmdb.read')
                return HttpResponseRedirect('/cmdb/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("用户失效")
        else:
            print "登录失败: {0}, {1}".format(username, password)
            return HttpResponse("用户登录失败")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'cmdb/login.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/cmdb/login')


