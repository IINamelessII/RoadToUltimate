from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('solutions/', views.solutions, name='solutions'),
    path('teachers/', views.teachers, name='teachers'),
    path('users/', views.users, name='users'),
    path('subjects/', views.subjects, name='subjects'),
    path('groups/', views.groups, name='groups'),
    path('solutions/<int:solution_id>/', views.solution, name='solution'),
    path('teachers/<int:teacher_id>/', views.teacher, name='teacher'),
    path('groups/<int:group_id>/', views.group, name='group'),
    path('subjects/<int:subjects_id>/', views.subjects, name='subjects'),
    path('users/<int:user_id>/', views.user, name='user'),
]
