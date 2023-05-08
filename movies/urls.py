from django.urls import path
from . import views 

urlpatterns = [
    path('',views.view_movies, name="view_movies" ),
    path('add_movie',views.add_movie, name="add_movie")
    
    # path('delete_mention/<int:myid>/',views.delete_mention, name = 'delete_mention'),
    # path('edit_mention/<int:myid>/',views.edit_mention, name = 'edit_mention'),
    # path('update_mention/<int:myid>/',views.update_mention, name = 'update_mention')
]