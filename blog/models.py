from django.db import models
from django.utils import timezone
from datetime import datetime

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default= timezone.now)
	published_date = models.DateTimeField(blank=True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


# Create your models here.
class Album(models.Model):

	"""https://github.com/marinho/aprendendo-django/blob/master/20-uma-galeria-de-imagens-simples-e-util.md
	um album é um pacote de imagens, ele tem um título e um slug para
	sua idenficacao."""

	class Meta:
		"""doctring for Meta"""
			ordering = ('titulo',)
		titulo = models.CharField(max_length=100)
		slug = models.SlugField(max_length=100, blank=True, unique=True)	

		def __unicode__(self):
			return self.titulo
			

class Image(models.Model):
		"""cada instancia desta classe contem uma imagem da galeria com seu respec
		tivo thumbnail(miniatura) e imagem em tambanho natural.
		Varias imagens podem conter dentro de um album"""
		
		class Meta:
			ordering = ('album','titulo',)