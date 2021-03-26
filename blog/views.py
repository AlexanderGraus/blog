from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{"posts":posts})

def post_detail(request,pk): #la variable se tiene que llamar exactamente pk porque asi la defini en urls 
    post = get_object_or_404(Post, pk = pk)
    return render(request,'blog/post_detail.html',{'post':post})
    # mando a renderizar la vista y le envio el post

def post_new(request):
    if request.method == 'POST':
        # significa que ya se envio la informacion del formulario a traves de post
        form = PostForm(request.POST)
        # reconstruyo el formulario con los datos que me llegan a traves de post

        if form.is_valid():
            post = form.save(commit=False) 
            # guarda el formulario pero con commit=false todavia no lo ingresa a la BD (falta guardar el usuario)
            post.author = request.user
            post.save()
            #ya esta ingresado el post al sitio

            return redirect('post_detail',pk=post.pk)
            # redirige a la pagina detalle del nuevo post
    else:
        form = PostForm()
    return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk= pk)
    # busco el post original en la BD
    if request.method != 'POST':
        # todavia no se actualizo el post, le cargo el post original
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST, instance=post)
        # ahora si guardo los datos actualizados del formulario
        if form.is_valid():
            # guardo el post editado
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail',pk = post.pk)
    return render(request,'blog/post_edit.html',{'form':form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull = True).order_by('created_date')
    # toma los posts no publicados
    return render(request,'blog/post_draft_list.html',{'posts':posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    get_object_or_404(Post,pk=pk).delete()
    return redirect('post_list')