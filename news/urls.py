from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name='home'),
    path('yangiliklar/', views.post_list, name='post_list'),
    path('yangilik/<slug:slug>/', views.post_detail, name='post_detail'),
    path('yangilik/<slug:slug>/ulashish/', views.post_share, name='post_share'),
    path('kategoriya/<slug:slug>/', views.category_posts, name='category'),
    path('tag/<str:tag>/', views.tag_posts, name='tag_posts'),
    path('qidiruv/', views.post_search, name='post_search'),
    path('biz-haqimizda/', views.about, name='about'),
    path('aloqa/', views.contact, name='contact'),
]
