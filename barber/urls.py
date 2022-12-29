from django.urls import path
from .import views
urlpatterns=[
    path('',views.barber_python, name="index")
]
