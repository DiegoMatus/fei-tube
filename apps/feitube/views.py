from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.feitube.models import Profile, Video, Comment
from apps.feitube.tasks import video_encode
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    videos = Video.objects.all()
    context = { 'videos': videos }
    return render(request, 'index.html', context)


@csrf_exempt
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            pass
    else:
        return redirect('index')

@login_required(login_url='/')
def logout_view(request):
	logout(request)
	return redirect('index')
	
@csrf_exempt
def signup_view(request):
	if request.method == "POST":
	    first_name = request.POST['first_name']
	    last_name = request.POST['last_name']
	    email = request.POST['email']
	    username = request.POST['username']
	    password = request.POST['password']
	    confirm_password = request.POST['password2']
	    profile_picture = request.FILES.get('profile_picture')

	    if password == confirm_password:
	    	password = make_password(password)
	    	confirm_password = make_password(confirm_password)

	    	user = User(username=username, first_name=first_name, last_name=last_name, email=email,
	    		password=password)
	    	user.save()

	    	profile = Profile(user=user, profile_picture=profile_picture)
	    	profile.save()

	return redirect(request.META.get('HTTP_REFERER'))
		

def search_view(request):
	if request.method == "POST":
		query = request.POST['search']
		video_results = Video.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query) | Q(description__icontains=query)).order_by('uploaded')
		context = { 'videos': video_results}
		return render(request, 'search.html', context)
	else:
		return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/')
def upload_view(request):
	return render(request, 'upload.html')

@csrf_exempt
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
        return redirect(request.META.get('HTTP_REFERER'))


@csrf_exempt
def public_comment_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		user = get_object_or_404(User, username=username)
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
		return redirect(request.META.get('HTTP_REFERER'))
		

def video_view(request, video_slug):
	video = get_object_or_404(Video, slug=video_slug)
	video.views += 1
	video.save()
	comments = video.video_comments.all()
	context = {'video' : video, 'comments' : comments}
	return render(request, 'video.html', context)

@login_required
def channel_view(request):
	pass
