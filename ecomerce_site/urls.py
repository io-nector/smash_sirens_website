from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('merch/',views.merch,name='merch')
]