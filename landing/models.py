from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from PIL import Image as PILImage
from ckeditor_uploader.fields import RichTextUploadingField


class Avaliacao(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/')
    avaliacao = models.TextField()
    estrelas = models.PositiveIntegerField(choices=[(i, i) for i in range(6)])

    pass

    def __str__(self):
        return self.nome


def validate_image(image):
    max_size = 2 * 1024 * 1024
    max_width = 1920
    max_height = 1080

    if image.size > max_size:
        raise ValidationError("O tamanho da imagem não pode exceder 2 MB.")

    img = PILImage.open(image)
    if img.width > max_width or img.height > max_height:
        raise ValidationError(
            f"As dimensões da imagem não podem exceder {max_width}x{max_height} pixels.")


class Article(models.Model):
    TIPO_CHOICES = [
        ('noticias', 'Notícias'),
        ('avisos', 'Avisos'),
        ('dicas', 'Dicas'),
    ]

    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    conteudo = RichTextUploadingField()
    imagem = models.ImageField(

        upload_to='noticias/', blank=False, validators=[validate_image])
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    tipo = models.CharField(
        max_length=10, choices=TIPO_CHOICES, default='noticias')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def format_data_publicacao(self):
        return self.data_publicacao.strftime("%d/%m/%Y, %H:%M")

    def __str__(self):
        return self.titulo
