
import threading
from django.shortcuts import render
from .models import MyModel
import logging

logger = logging.getLogger(__name__)

def create_model_instance(request):
    def worker():
        MyModel.objects.create(name="Test")
    
    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()   
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')