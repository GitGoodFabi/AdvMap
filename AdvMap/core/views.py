from django.shortcuts import render
from .models import Crag, InstaRoute
# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to AdvMap - Your Adventure Mapping Tool!")
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about_view(request):
    about_text = """
AdvMap <del>is a </del> *may become* a digital toolset for modern adventure seekers.

Whether you're motorbiking across **Africa** or bouldering in *Fontainebleau* – this is your map.

## Features

- Interactive action sport map (coming some day)
- Route logging (coming soon)
- Community uploaded spots and crags (coming soon)  
- Blog with adventure stories (right now its more stories about what I learned while building this)
- Open source and free to use (always)
- maybe I'll put up an
 hangboard timer here for fun
"""
    return render(request, "core/about.html", {"about_text": about_text})

def about(request):
    return render(request, 'core/map.html', {'routes': routes})

def map_view(request):
    crags = Crag.objects.all()
    return render(request, 'core/map.html', {'crags': crags})

def map_view(request):
    routes = InstaRoute.objects.all()
    return render(request, 'core/map.html', {'routes': routes})


from .models import Post

def blog_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'core/blog_list.html', {'posts': posts})

#Blog posts importieren:
from django.shortcuts import get_object_or_404

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'core/blog_detail.html', {'post': post})

