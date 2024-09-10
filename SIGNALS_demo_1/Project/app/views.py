from django.shortcuts import render
from .models import MyModel

def create_model_instance(request):
    MyModel.objects.create(name="Test")
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')