from django.urls import path
from . import views
# listings\
urlpatterns = [
    path('', views.index, name='index'),
    path('published', views.published, name='published'),
]
