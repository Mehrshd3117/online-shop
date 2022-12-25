# Django packages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Local apps
from .models import User
from .forms import UserLoginForm, UserRegistrationForm


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], phone=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "Your logged in is successfully", 'success')
                return redirect('home:home')

        context = {'form': form}
        return render(request, self.template_name, context)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home:home')


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                email=cd['email'], phone=cd['phone'], password=cd['password1']
            )
            if user is not None:
                login(request, user)
            user.save()
            messages.success(request, "Your registred is successfully.", 'success')
            return redirect('home:home')

        context = {'form': form}
        return render(request, self.template_name, context)
