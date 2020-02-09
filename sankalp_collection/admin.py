from django.contrib import admin
from .models import articles, ArticleCategory
from tinymce.widgets import TinyMCE
from django.db import models


class articleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/Description", {"fields": ['name', 'description']}),
        ('Details', {"fields": ['image', 'image2', 'image3', 'price', 'link', 'series_name']}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(articles, articleAdmin)
admin.site.register(ArticleCategory)
