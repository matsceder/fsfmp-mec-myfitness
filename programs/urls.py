from django.urls import path
from . import views


urlpatterns = [
    path('', views.programs, name='programs'),
    path('program/<int:program_id>/', views.program, name='program'),
    path('add_post/', views.add_program, name='add_program'),
]
