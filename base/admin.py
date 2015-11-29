from django.contrib import admin
from imagekit.admin import AdminThumbnail
from base import models
# Register your models here.

class DestaquePrincipalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'is_principal', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagem_thumb')

class DestaqueSecundarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'ativo', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagem_thumb')

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco', 'descricao', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagem_thumb')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco', 'descricao', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='imagem_thumb')

admin.site.register(models.DestaquePrincipal, DestaquePrincipalAdmin)
admin.site.register(models.DestaqueSecundario, DestaqueSecundarioAdmin)
admin.site.register(models.Servico, ServicoAdmin)
admin.site.register(models.Produto, ProdutoAdmin)
