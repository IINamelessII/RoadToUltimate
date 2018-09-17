from django.urls import path
from . import views
import sys
sys.path.append('..')
from main import views as views_main

urlpatterns = [
    path('', views_main.index, name='go2Main'),
    path('palevo/', views.index, name='index'),
    path('palevo/solutions/', views.solutions, name='solutions'),
    path('palevo/teachers/', views.teachers, name='teachers'),
    path('palevo/users/', views.users, name='users'),
    path('palevo/subjects/', views.subjects, name='subjects'),
    path('palevo/groups/', views.groups, name='groups'),
    path('palevo/solutions/<int:solution_id>/', views.solution, name='solution'),
    path('palevo/teachers/<int:teacher_id>/', views.teacher, name='teacher'),
    path('palevo/groups/<int:group_id>/', views.group, name='group'),
    path('palevo/subjects/<int:subject_id>/', views.subject, name='subject'),
    path('palevo/users/<int:user_id>/', views.user, name='user'),
]
