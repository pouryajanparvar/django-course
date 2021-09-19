from django.shortcuts import render
# Create your views here.


def Home_page(request):
    return render(request, 'A/home_page.html', {})