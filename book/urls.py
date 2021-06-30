from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListCreate.as_view()),
    path('<int:pk>', views.BookRetrieveUpdateDestroyAPIView.as_view()),
]