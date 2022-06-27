from django.urls import path

from movies import views


app_name='movies'
urlpatterns = [
    path('', views.MoviesListView.as_view(), name='movies-list'),
    path('movies/add/', views.MoviesCreateView.as_view(), name='movies-add'),
    path('movies/<int:pk>/detail', views.MoviesDetailView.as_view(), name='movies-detail'),
    path('movies/<int:pk>/update', views.MoviesUpdateView.as_view(), name='movies-update'),
    path('movies/<int:pk>/delete', views.MoviesDeleteView.as_view(), name='movies-delete'),
    path('search', views.search, name='search'),
    path('movies/<int:pk>/comment/', views.AddCommentView.as_view(), name='add-comment'),
]