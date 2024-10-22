from django.shortcuts import render

# Create your views here.


def home_views(request):
    template_view = "index.html"
    return render(request,template_name=template_view)