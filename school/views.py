from django.shortcuts import render
from school.models import Post,Photo,File


# Create your views here.
def index(request):
	posts = Post.objects.all()
	photos = Photo.objects.all()
	files = File.objects.all()
	return render(request,'school/index.html',{'posts':posts, 'photos':photos, 'files':files})

def about(request):
	return render(request,'school/about.html')

def gallery(request):
	return render(request,'school/gallery.html')

def news(request):
	return render(request,'school/news.html')

def contact(request):
	return render(request,'school/contact.html')

