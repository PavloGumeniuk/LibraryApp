from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListCreate.as_view()),
    path('order/', views.OrderRetrieveUpdateDestroyAPIView.as_view()),
]