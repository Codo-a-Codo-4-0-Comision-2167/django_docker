from django.shortcuts import render
from django.http import HttpResponse
import json

from polls.models import Music

# Create your views here.
def index(request):
    #return render(request, 'polls/index.html')
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

## Vamos a definir nuestro CRUD
# Create, Read, Update, Delete
def read(request, id):
    myMusic = Music.objects.get(id=id)
    #myMusicJSON = json.load(myMusic)
    return HttpResponse("%s." % myMusic)

def delete(request, id):
    myMusic = Music.objects.get(id=id)
    myMusic.delete()
    return HttpResponse("Music with id: %s deleted" % id)

def create(request):
    # modifcar el metodo create para recibir data solo por post
    # Y mediante un form html cargar la data del artista, album y genero.
    myMusic = Music(artist="My Artist", album="My Album", genre="Rock")
    myMusic.save()
    return HttpResponse("Music with id: %s created" % myMusic.id)

def update(request, id):
    myResponse = HttpResponse(" You must use POST METHOD")
    
    if request.method == 'POST':
        myMusic = Music.objects.get(id=id)
        myMusic.artist = request.POST.get('artist')
        myMusic.album = request.POST.get('album')
        myMusic.genre = request.POST.get('genre')
        myMusic.save()
        myResponse = HttpResponse("Music with id: %s updated" % myMusic.id)
    
    return myResponse
   