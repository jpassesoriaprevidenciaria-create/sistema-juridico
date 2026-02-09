from django.contrib import admin
from .models import Prazo

@admin.register(Prazo)
class PrazoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'data_final')

