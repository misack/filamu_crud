from django.shortcuts import render , redirect
from . models import Movie

# Create your views here.

def view_movies(request):
    movies = Movie.objects.all()

    context = {
        'movies':movies
    }

    return render(request, 'movies/view_movies.html', context)

def add_movie(request):
	if request.method == "POST":
		
 
		title = request.POST['title']
		release_date = request.POST.get('release_date')
		directors = request.POST.get('directors')
		actors = request.POST['actors']
		writers = request.POST.get('writers')
		genres = request.POST['genres']
		storyline = request.POST.get('storyline')
		trailer_url = request.POST['trailer_url']
		# cover = request.POST['cover']   
		cover = request.FILES['cover'] 
		
		mention=Movie(
			title = title, 
            release_date = release_date,
            directors = directors,
            actors = actors,
            writers = writers,
            genres = genres,
            storyline = storyline,
            trailer_url = trailer_url,
		    cover = cover
	    )
		mention.save();


		return redirect(view_movies)

	else:
		pass
	return render(request,'movies/add_movie.html')