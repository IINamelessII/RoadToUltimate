from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:movie_id>', views.movie),
    # path('genres/<int:genre_id>', views.genre, name='genre'),
    # path('genres', views.genres, name='genres'),
    # path('directors/<int:director_id>', views.director, name='director'),
    # path('directors', views.directors, name='directors'),
    # path('profiles/<str:username>', views.profile, name='profile'),
    # path('', v.index, name='index'),
    # path('login', v.login_view, name='login'),
    # path('logout', v.logout_view, name='logout')
    ]
