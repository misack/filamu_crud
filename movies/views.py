from django.shortcuts import render , redirect
from django.contrib import messages

from . models import Movie


from django.core.files.storage import FileSystemStorage


from django.core.paginator import Paginator
# Create your views here.

def view_movies(request):
    movies = Movie.objects.all()

    paginator = Paginator(movies,10)
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)

    
    context = {
        'movies':movies
    }

    return render(request, 'movies/view_movies.html',context)


def view_movie(request,pk):
    movie =Movie.objects.get(id=pk)
    context = {
        'movie':movie,
    }
    return render(request,'movies/view_movie.html', context)


def add_movie(request):
   
    if request.method == 'POST' and request.FILES['upload']:
        
        upload = request.FILES['upload'] 
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)

        title = request.POST['title']
        release_date = request.POST.get('release_date')
        directors = request.POST.get('directors')
        actors = request.POST['actors']
        writers = request.POST.get('writers')
        genres = request.POST['genres']
        storyline = request.POST.get('storyline')
        trailer_url = request.POST['trailer_url']
        
        mention=Movie(
            title = title, 
            release_date = release_date,
            directors = directors,
            actors = actors,
            writers = writers,
            genres = genres,
            storyline = storyline,
            trailer_url = trailer_url,
            cover = file
        )
        
        mention.save()
        messages.info(request,'A movie is added successfuly')
        return render(request, 'movies/add_movie.html', {
            'uploaded_file_url': file_url
        })

        # return redirect(view_movies)

    else:
        pass
    
    return render(request,'movies/add_movie.html')



def edit_movie(request,pk):
    movie =Movie.objects.get(id=pk)
    context = {
        'movie':movie,
    }
    return render(request,'movies/edit_movie.html', context)

def update_movie(request,myid):

    if request.method == 'POST' and request.FILES['upload']:
        movie = Movie.objects.get(id=myid)

        upload = request.FILES['upload'] 
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        # file_url = fss.url(file)

        movie.title = request.POST['title']
        movie.release_date = request.POST.get('release_date')
        movie.directors = request.POST.get('directors')
        movie.actors = request.POST['actors']
        movie.writers = request.POST.get('writers')
        movie.genres = request.POST['genres']
        movie.storyline = request.POST.get('storyline')
        movie.trailer_url = request.POST['trailer_url']
        movie.cover = file
        movie.save()

        messages.info(request,'A movie is updated successfuly')

    return redirect(view_movies)


def delete_movie(request,myid):
	movie = Movie.objects.get(id=myid)
	movie.delete()
	messages.info(request,'A movie is deleted successfuly')
	return redirect(view_movies)