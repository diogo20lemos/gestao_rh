from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from apps.core.serializers import UserSerializer, GroupSerializer
from .tasks import send_relatorio

from apps.departamentos.models import Departamento
from django.core import serializers
from django.http import HttpResponse


@login_required
def home(request):
    data = {'usuario': request.user}
    funcionario = request.user.funcionario
    data['total_funcionarios'] = funcionario.empresa.total_funcionarios
    data['total_funcionarios_ferias'] = \
        funcionario.empresa.total_funcionarios_ferias
    data['total_funcionarios_doc_pendente'] =\
        funcionario.empresa.total_funcionarios_doc_pendente
    return render(request, 'core/index.html', data)


def celery(request):
    send_relatorio.deley()
    return HttpResponse('Tarefa incluída na fila para execução.')


def departamento_ajax(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamento_ajax.html',
                  {'departamentos': departamentos})


def filtra_funcionarios(request):
    depart = request.GET['outro_param']
    departamento = Departamento.objects.get(id=depart)

    qs_json = serializers.serialize('json', departamento.funcionario_set.all())
    return HttpResponse(qs_json, content_type='application/json')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


