from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthorListCreate.as_view()),
    path('<int:pk>', views.AuthorRetrieveUpdateDestroyAPIView.as_view()),
]
