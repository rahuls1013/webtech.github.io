from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('news/',views.news),
    path('video/',views.video),
    path('contactus/',views.contactus),

]