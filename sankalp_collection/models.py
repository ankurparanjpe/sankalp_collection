from django.db import models


class ArticleCategory(models.Model):
    category_title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    category_link = models.CharField(max_length=100)
    category_image = models.ImageField(blank=True)

    class Meta:
        verbose_name_plural = "ArticleCategories"

    def __str__(self):
        return self.category_title


class articles(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    price = models.CharField(max_length=50)
    link = models.SlugField()
    series_name = models.ForeignKey(ArticleCategory, default=1, on_delete=models.SET_DEFAULT)
    color = models.TextField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "articles"

    def __str__(self):
        return self.name
