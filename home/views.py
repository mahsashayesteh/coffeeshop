from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'Home.html', {})

def aboutus_view(request, *args, **kwargs):
    return render(request, 'aboutUs.html', {})

def contactus_view(request, *args, **kwargs):
    return render(request, 'contactUs.html', {})