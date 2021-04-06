from django.shortcuts import render
from django.views import View


class HomeView(View):

    def get(self, request):
        return render(self.request, 'routes/home.html')
