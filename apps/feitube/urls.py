from django.conf.urls import include, url, patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('apps.feitube.views',
    url(r'^$', 			'index', 		name='index'),
    url(r'^login/$', 	'login_view', 	name='login'),
    url(r'^logout/$', 	'logout_view', 	name='logou'),
    url(r'^signup/$', 	'signup_view', 	name='signup'),
    url(r'^search/$', 	'search_view', 	name='seach'),
    url(r'^upload/$', 	'upload_view', 	name='upload'),
    url(r'^watch/(?P<video_slug>[\w|\W]+)/$',		'video_view',		name='video'),
    url(r'^channel/(?P<username_slug>[\w|\W]+)/$',	'channel_view',		name='channel'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 	#Servir estáticos en desarrollo