from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.feitube.models import Profile, Video

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
	return render(request, 'upload.html')

@csrf_exempt
def upload_video_view(request):
    if request.method == 'POST':
        video_title = request.POST.get("video_title")
        video_tags = request.POST.get("video_tags")
        video_description = request.POST.get("video_description")
        video_path = request.FILES['video']
        user = request.user
        video_profile = Profile.objects.get(user=user)

        video = Video(title=video_title, tags=video_tags, description=video_description,
        			path=video_path, profile=video_profile)

        video.save()
        return redirect('upload')
        #return JsonResponse(dict({'video_path' : video_title}))
    else:
        return render(request, 'index.html')


def video_view(request, video_slug):
	video = Video.objects.get(slug=video_slug)
	context = {'video' : video}
	return render(request, 'video.html', context)

def channel_view(request):
	pass
