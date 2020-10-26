from django.contrib import admin
from .models import Teste, RegistroUsuarios


class RegistroUsuariosAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return RegistroUsuarios.objects.using('antigo').all()

admin.site.register(Teste)
admin.site.register(RegistroUsuarios, RegistroUsuariosAdmin)