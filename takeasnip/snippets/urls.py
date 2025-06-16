from django.urls import path
from . import views

urlpatterns = [
    path('', views.snippet_list, name='snippet_list'),
    path('<int:pk>/delete', views.snippet_delete, name='snippet_delete'),
    path('<int:pk>/vote/', views.vote_snippet, name='vote_snippet'),
    path('<int:pk>/', views.snippet_detail, name='snippet_detail'),
    path('new/', views.snippet_create, name='snippet_create'),
]