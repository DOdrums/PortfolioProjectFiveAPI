from django.urls import path
from song import views

urlpatterns = [
    path("songs/", views.SongList.as_view()),
    path("songs/<int:pk>/", views.SongDetail.as_view()),
]
