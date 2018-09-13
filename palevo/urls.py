from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('solutions/', views.solutions, name='solutions'),
    path('solutions/<int:solution_id>/', views.solution, name='solution'),
]
