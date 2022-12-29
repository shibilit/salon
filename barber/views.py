from django.shortcuts import render

# Create your views here.
def barber_python(request):
    return render(request,'barbertemplates/python.html')
