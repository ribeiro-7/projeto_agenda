from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from contact.forms import RegisterForm, UserUpdateForm


def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered Successfully')
            return redirect('contact:login')

    context = {
        'form': form
    }

    return render(
        request,
        'contact/register.html',
        context
    )

def login(request):

    form = AuthenticationForm(request)

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('contact:index')
        else:
            messages.error(request, 'Login invalid')

    context = {
        'form': form
    }

    return render(
        request,
        'contact/login.html',
        context
    )

@login_required(login_url='contact:login')
def user_update(request):

    form = UserUpdateForm(instance=request.user)

    if request.method == 'POST':

        form = UserUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():

            form.save()
            messages.success(request, 'Updated Successfully')
            return redirect('contact:user_update')
        else:
            messages.error(request, 'Update invalid')


    context = {
        'form': form
    }

    return render(
        request,
        'contact/user_update.html',
        context
    )

@login_required(login_url='contact:login')
def logout(request):
    
    auth.logout(request)

    return redirect('contact:login')