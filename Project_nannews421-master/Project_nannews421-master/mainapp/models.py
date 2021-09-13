from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Source(models.Model):
    nom_site = models.CharField(max_length=255)
    lien = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = 'Source'
        verbose_name_plural = 'Sources'

    def __str__(self):
        return self.nom_site


class Article(models.Model):
    titre = models.CharField(max_length=255)
    source_image = models.TextField()
    lien_detail = models.TextField()
    categorie = models.ForeignKey('mainapp.Article', related_name='categorie_article', on_delete=models.CASCADE)
    description = HTMLField()
    date_publication = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre



class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    date_publication = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta():
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nom