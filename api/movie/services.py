from models.movie import Movie, Genres

def getAllMovie():
    movie = Movie.objects.all()
    return movie

def singleMovie(pk):
    movie = Movie.objects.get(pk=pk)
    return movie

def filterMovie(query):
    movie = Movie.objects.filter(title__icontains=query)
    return movie

def getGenre():
    genre = Genres.objects.all()
    return genre
