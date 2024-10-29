# api/home/home_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.home.value_const import LOGING_URL

@login_required
def home_view(request):
    return render(request, 'index.html')
