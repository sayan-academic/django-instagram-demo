from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

#added line
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts': all_posts})

def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/details.html', {'post': post})

def postform1(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    return render(request, 'posts/postform1.html', {'postform': form})