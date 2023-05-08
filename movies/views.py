from django.shortcuts import render , redirect
from . models import Movie


from django.core.files.storage import FileSystemStorage


from django.core.paginator import Paginator
# Create your views here.

def view_movies(request):
    movies = Movie.objects.all()

    paginator = Paginator(movies,2)
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)

    
    context = {
        'movies':movies
    }

    return render(request, 'movies/view_movies.html', context)

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
        # cover=request.POST.get('cover')
        # cover = request.FILES['cover']
        
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
        return render(request, 'movies/add_movie.html', {
            'uploaded_file_url': file_url
        })

        # return redirect(view_movies)

    else:
        pass
    return render(request,'movies/add_movie.html')