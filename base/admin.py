from django.contrib import admin
from imagekit.admin import AdminThumbnail
from base import models
# Register your models here.

class DestaquePrincipalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'link', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagem_thumb')

class DestaqueSecundarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'link', 'ativo', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagem_thumb')

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagem_thumb')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagem_thumb')

class PapelariaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagem_thumb')

admin.site.register(models.DestaquePrincipal, DestaquePrincipalAdmin)
admin.site.register(models.DestaqueSecundario, DestaqueSecundarioAdmin)
admin.site.register(models.Servico, ServicoAdmin)
admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Papelaria, PapelariaAdmin)
