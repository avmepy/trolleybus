from django.shortcuts import render
from django.views import View
from accounts.forms import UserLoginForm
from accounts import services


class LoginView(View):

    def get(self, request):
        return render(self.request, 'accounts/login.html', {'form': UserLoginForm})

    def post(self, request):

        form = UserLoginForm(request.POST)

        if form.is_valid():
            return services.login_user(self.request, form)

        # else
        return render(self.request, 'accounts/login.html', {'form': UserLoginForm})


class LogoutView(View):

    def get(self, request):
        return services.logout_user(self.request)


class ProfileView(View):

    def get(self):

        return render(self.request, 'accounts/profile.html')

