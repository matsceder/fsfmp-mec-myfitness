from django.urls import path
from . import views


urlpatterns = [
    path('', views.programs, name='programs'),
    path('<int:program_id>/', views.program, name='program'),
]
