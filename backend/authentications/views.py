from django.shortcuts import render
from django.views import View

# Create your views here.

class UserRegistrationView(View):

    def get(request,*args, **kwargs):

        return render()