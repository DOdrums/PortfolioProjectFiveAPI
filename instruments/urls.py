from django.urls import path
from instruments import views

urlpatterns = [
    path("instruments/", views.InstrumentList.as_view()),
    path("instruments/<int:pk>/", views.InstrumentDetail.as_view()),
]
