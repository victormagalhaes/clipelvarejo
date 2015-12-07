# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Destaque(models.Model):
	titulo = models.CharField(max_length=100)
	subtitulo = models.CharField(max_length=100)
	link = models.CharField(max_length=200, default='')
	imagem = models.ImageField(upload_to=settings.IMAGE_UPLOAD_DESTAQUE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class DestaquePrincipal(Destaque):
	imagem_full = ImageSpecField(
		source='imagem', processors=[ResizeToFill(1280, 700)], format='JPEG', options={'quality': 100}
	)
	imagem_thumb = ImageSpecField(
		source='imagem', processors=[ResizeToFill(365, 200)], format='JPEG', options={'quality': 100}
	)

	class Meta:
		verbose_name = 'Destaque Principal'
		verbose_name_plural = 'Destaques Principais'


class DestaqueSecundario(Destaque):
	imagem_full = ImageSpecField(
		source='imagem', processors=[ResizeToFill(600, 400)], format='JPEG', options={'quality': 100}
	)
	imagem_thumb = ImageSpecField(
		source='imagem', processors=[ResizeToFill(300, 200)], format='JPEG', options={'quality': 100}
	)
	ativo = models.BooleanField(default=False, verbose_name='Destaque ativo')

	def save(self, *args, **kwargs):

		if self.ativo:
			destaques = DestaqueSecundario.objects.filter(ativo=True).order_by('-updated_at').exclude(id=self.id)
			if len(destaques) == 2:
				destaques[1].ativo = False
				destaques[1].save()

		super(DestaqueSecundario, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Destaque Secundário'
		verbose_name_plural = 'Destaques Secundários'


class EntidadeExibicao(models.Model):
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	imagem = models.ImageField(upload_to=settings.IMAGE_UPLOAD_SERVICOS)

class Servico(EntidadeExibicao):
	imagem_full = ImageSpecField(
		source='imagem', processors=[ResizeToFill(900, 650)], format='JPEG', options={'quality': 100}
	)
	imagem_thumb = ImageSpecField(
		source='imagem', processors=[ResizeToFill(276, 200)], format='JPEG', options={'quality': 100}
	)

	class Meta:
		verbose_name = 'Serviço'
		verbose_name_plural = 'Serviços'


class Produto(EntidadeExibicao):
	imagem_full = ImageSpecField(
		source='imagem', processors=[ResizeToFill(700, 700)], format='JPEG', options={'quality': 100}
	)

	imagem_thumb = ImageSpecField(
		source='imagem', processors=[ResizeToFill(263, 263)], format='JPEG', options={'quality': 100}
	)

	class Meta:
		verbose_name = 'Presente'
		verbose_name_plural = 'Presentes'
