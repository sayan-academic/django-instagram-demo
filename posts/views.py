from django.shortcuts import render
from .models import Post

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