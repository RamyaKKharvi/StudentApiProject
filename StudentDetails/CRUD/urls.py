from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentCreateAndRetrieve.as_view()),
    path('delete/<student_id>', views.StudentDeleteAndUpdate.as_view()),
    path('update/<student_id>', views.StudentDeleteAndUpdate.as_view()),
]