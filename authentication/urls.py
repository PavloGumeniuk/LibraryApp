from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthenticationList.as_view()),
    path('<int:pk>/', views.AuthenticationRetrieve.as_view()),
    path('<int:pk>/update/', views.AuthenticationUpdate.as_view()),
    path('<int:pk>/destroy/', views.AuthenticationDestroy.as_view()),
    path('create/', views.AuthenticationCreate.as_view()),
]