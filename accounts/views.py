from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from accounts.forms import UserLoginForm
from accounts import services
from trolleybus2.settings import LOGIN_URL


class LoginView(View):

    def get(self, request):
        return render(self.request, 'accounts/login.html', {'form': UserLoginForm})

    def post(self, request):

        form = UserLoginForm(request.POST)

        if form.is_valid():
            return services.login_user(self.request, form)

        # else
        return render(self.request, 'accounts/login.html', {'form': UserLoginForm})


class LogoutView(LoginRequiredMixin, View):
    login_url = LOGIN_URL

    def get(self, request):
        return services.logout_user(self.request)


class ProfileView(LoginRequiredMixin, View):
    login_url = LOGIN_URL

    def get(self):

        return render(self.request, 'accounts/profile.html')

