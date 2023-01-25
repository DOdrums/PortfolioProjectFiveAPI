from django.urls import path
from mics import views

urlpatterns = [
    path("mics/", views.MicList.as_view()),
    path("mics/<int:pk>/", views.MicDetail.as_view()),
]
