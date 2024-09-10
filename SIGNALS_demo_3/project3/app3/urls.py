
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Assuming you have an index view
    path('create-model-instance/', views.create_model_instance, name='create_model_instance'),
]
