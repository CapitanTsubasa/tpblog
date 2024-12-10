from django.shortcuts import render, get_object_or_404
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm()
    return render(request, 'blog/agregar_autor.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'blog/agregar_categoria.html', {'form': form})

def agregar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'blog/agregar_post.html', {'form': form})

def buscar_post(request):
    query = request.GET.get('q')
    resultados = Post.objects.filter(titulo__icontains=query) if query else None
    return render(request, 'blog/buscar_post.html', {'resultados': resultados, 'query': query})


