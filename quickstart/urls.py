from django.urls import path
from quickstart import views

urlpatterns = [
    path('api', views.StudentsView.as_view())
]