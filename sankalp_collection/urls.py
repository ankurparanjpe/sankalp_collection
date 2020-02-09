from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.homepage, name='homepage'),
    path('<category_link>', views.category_link, name='category_link'),
    path('<link>', views.link, name='link'),
]
