from django.shortcuts import redirect, render
from django.contrib import messages

from contact.forms import RegisterForm


def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered Successfully')
            return redirect('contact:index')

    context = {
        'form': form
    }

    return render(
        request,
        'contact/register.html',
        context
    )