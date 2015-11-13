from django.shortcuts import render

# Create your views here.
def index(request):
    #languages = Language.objects.all() #Hacerlo global
    #context = { 'languages': languages }
    return render(request, 'index.html')


def login_view(request):
	#languages = Language.objects.all()
	#language = get_object_or_404(Language, slug = language_slug)
	#categories = language.categories.all()
	#context = { 'languages': languages, 'language': language, 'categories': categories }
	return render(request, 'categories.html')

def logout_view(request):
	pass
	
def signup_view(request):
	pass

def search_view(request):
	pass

def upload_view(request):
	pass

def video_view(request):
	pass

def channel_view(request):
	pass
