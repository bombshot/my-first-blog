from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^hello/', 'myapp.views.hello', name = 'hello'),
	]