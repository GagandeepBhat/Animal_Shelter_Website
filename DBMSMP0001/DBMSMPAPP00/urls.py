from django.urls import path
from . import views
from DBMSMPAPP00.views import animalshelters
from DBMSMPAPP00.views import adoption

urlpatterns = [
    path('', views.index, name='index'),
    path('counter',views.counter,name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('animalshelterspage',views.animalshelters,name='animalshelterspage'),
    path('adoption',views.adoption,name='adoption'),
    path('volunteering',views.volunteering,name='volunteering'),

]
