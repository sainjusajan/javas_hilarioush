from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^about/$',views.about, name='about'),
	url(r'^gallery/$',views.gallery, name='gallery'),
	url(r'^news/$',views.news, name='news'),
	url(r'^contact/$',views.contact, name='contact'),
]