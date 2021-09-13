from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin):
	list_display = ('nom_site', 'lien','date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['lien', 'status']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('titre', 'source_image', 'lien_detail', 'categorie', 'description', 'date_publication','date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['status']


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
	list_display = ('nom', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['status']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('nom', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['status']