from django.urls import path
from . import views
app_name = 'A'
urlpatterns = [
    path('', views.Home_page, name='home')
]