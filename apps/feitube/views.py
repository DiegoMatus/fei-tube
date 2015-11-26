from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.feitube.models import Profile, Video, Comment
from apps.feitube.tasks import video_encode
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #languages = Language.objects.all() #Hacerlo global
    #context = { 'languages': languages }
    return render(request, 'index.html')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('index')
        else:
            pass
    else:
        return redirect('index')

#@login_required(login_url='/')
def logout_view(request):
	logout(request)
	return redirect('index')
	
def signup_view(request):
	pass

def search_view(request):
	pass

#@login_required(login_url='/')
def upload_view(request):
	return render(request, 'upload.html')

#@csrf_exempt
def upload_video_view(request):
    if request.method == 'POST':
        user = request.user
        video_profile = Profile.objects.get(user=user)

        video_title = request.POST.get("video_title")
        video_tags = request.POST.get("video_tags")
        video_description = request.POST.get("video_description")
        video_path = request.FILES['video']

        video = Video(title=video_title, tags=video_tags, description=video_description,
        			path=video_path, profile=video_profile, views=0)

        video.save()
        video.generic_path = video.path.url.split('.')[-2]
        video.save()

        video_encode.delay(video.path.url)
        return redirect('upload')
        #return JsonResponse(dict({'video_path' : video_title}))
    else:
        return render(request, 'index.html')

#@login_required
@csrf_exempt
def public_comment_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		user = User.objects.get(username=username)
		comment_profile = Profile.objects.get(user=user)

		video = request.POST.get('video')
		comment_video = Video.objects.get(slug=video)

		comment = request.POST.get('comment')

		new_comment = Comment(video=comment_video, profile=comment_profile, comment=comment)
		new_comment.save()
		
		data = {
			'username': username,
			'video': video,
			'comment': comment,
			'published': new_comment.published,
			'profile_picture': comment_profile.profile_picture.url
		}
		return JsonResponse(data)
	else:
		return render(request, 'index.html')
		

def video_view(request, video_slug):
	video = Video.objects.get(slug=video_slug)
	video.views += 1
	video.save()
	comments = video.video_comments.all()
	context = {'video' : video, 'comments' : comments}
	return render(request, 'video.html', context)

#@login_required
def channel_view(request):
	pass
