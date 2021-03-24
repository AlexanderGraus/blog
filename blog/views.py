from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{"posts":posts})

def post_detail(request,pk): #la variable se tiene que llamar exactamente pk porque asi la defini en urls 
    post = get_object_or_404(Post, pk = pk)
    return render(request,'blog/post_detail.html',{'post':post})
    # mando a renderizar la vista y le envio el post
