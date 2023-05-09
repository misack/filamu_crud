from django.urls import path
from . import views 

urlpatterns = [
    path('',views.view_movies, name="view_movies" ),
    path('add_movie',views.add_movie, name="add_movie"),
    path('view_movie/<int:pk>',views.view_movie, name="view_movie"),
    path('edit_movie/<int:pk>',views.edit_movie, name="edit_movie"),
    path('update_movie/<int:myid>/',views.update_movie, name = 'update_movie'),
    path('delete_movie/<int:myid>/',views.delete_movie, name = 'delete_movie')
]