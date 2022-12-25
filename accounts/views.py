# Django packages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
# Local apps
from .models import User
from .forms import UserLoginForm


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
                return redirect('home:home')

        context = {'form': form}
        return render(request, self.template_name, context)
