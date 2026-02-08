from django.contrib import admin
from .models import Prazo

admin.site.register(Prazo)
from django.contrib import admin
from .models import Cliente, Processo, Prazo

admin.site.register(Cliente)
admin.site.register(Processo)
admin.site.register(Prazo)
