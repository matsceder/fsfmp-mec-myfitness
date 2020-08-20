from django.urls import path
from . import views


urlpatterns = [
    path('', views.programs, name='programs'),
    path('program/<int:program_id>/', views.program, name='program'),
    path('add_post/', views.add_program, name='add_program'),
    path('edit_post/<int:program_id>/', views.edit_program, name='edit_program'),
    path('delete_post/<int:program_id>/', views.delete_program, name='delete_program'),
    path('program_subscribe/', views.program_subscribe, name='program_subscribe'),
]
