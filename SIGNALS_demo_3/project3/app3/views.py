
from django.db import transaction
from django.shortcuts import render
from .models import MyModel
import logging

logger = logging.getLogger(__name__)

def create_model_instance(request):
    with transaction.atomic():
        MyModel.objects.create(name="Test")
    
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')
