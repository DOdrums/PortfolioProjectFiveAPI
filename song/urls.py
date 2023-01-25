from django.urls import path
from song import views

urlpatterns = [
    path("songs/", views.PostList.as_view()),
    path("songs/<int:pk>/", views.PostDetail.as_view()),
]
