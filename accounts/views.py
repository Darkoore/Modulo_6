from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login

def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        return redirect('dashboard')

    return render(request, 'accounts/register.html', {'form': form})