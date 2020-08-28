from django.urls import path, include
from .views import (
    DepartamentosList,
    DepartamentosCreate,
    DepartamentoUpdate,
    DepartamentoDelete,
)

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentosCreate.as_view(), name='create_departamento'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento'),
    path('update/<int:pk>',
         DepartamentoUpdate.as_view(), name='update_departamento'),


 ]
