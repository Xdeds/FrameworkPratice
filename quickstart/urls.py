from django.urls import path
from quickstart import views

urlpatterns = [
    path('list/', views.StudentsListView.as_view()),
    path('create/', views.StudentsCreateView.as_view()),
    path('up/<int:pk>', views.StudentsUpdateView.as_view()),
    path('destroy/<int:pk>', views.StudentsDeleteView.as_view()),
    path('retrieve/<int:pk>', views.StudentsRetriveView.as_view())
]