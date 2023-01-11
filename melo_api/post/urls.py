from django.urls import path
from post import views

urlpatterns = [
    path("posts/", views.PostList.as_view()),
    path("posts/<int:pk>/", views.PostDetail.as_view()),
]
