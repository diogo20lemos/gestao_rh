from django.urls import path, include
from .views import home, celery, departamento_ajax, filtra_funcionario


urlpatterns = [
    path('', home, name='home'),
    path('celery/', celery, name='celery'),
    path('departamento-ajax/', departamento_ajax, name='departamento_ajax'),
    path('filtra-funcionario', filtra_funcionario, name='filtra_funcionario'),


]
