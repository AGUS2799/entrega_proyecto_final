from django.urls import path

from series import views


app_name='series'
urlpatterns = [
    path('series/', views.SeriesListView.as_view(), name='series-list'),
    path('series/add/', views.SeriesCreateView.as_view(), name='series-add'),
    path('series/<int:pk>/detail', views.SeriesDetailView.as_view(), name='series-detail'),
    path('series/<int:pk>/update', views.SeriesUpdateView.as_view(), name='series-update'),
    path('series/<int:pk>/delete', views.SeriesDeleteView.as_view(), name='series-delete'),
    path('search', views.search, name='search'),
    path('series/<int:pk>/comment/', views.AddCommentView.as_view(), name='add-comment'),
]