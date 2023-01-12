from django.urls import path
from comment import views

urlpatterns = [
    path("comments/", views.CommentList.as_view()),
    path("comments/<int:pk>/", views.CommentDetail.as_view()),
]
