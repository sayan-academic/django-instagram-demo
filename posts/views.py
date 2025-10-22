from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.forms import formset_factory, modelformset_factory

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
            post = form.save()
            messages.success(request, f"New Post Successfully created : {post.name}!!")
            return redirect('posts:index')
    else:
        form = PostForm()
    return render(request, 'posts/postform1.html', {'postform': form})

def postformset(request):
    PostFormSet = modelformset_factory(Post, form=PostForm, extra=2, max_num=2)
    if request.method == 'POST':
        formset = PostFormSet(request.POST, request.FILES)
        if formset.is_valid():
            postset = formset.save()
            added_posts = [post.name for post in postset]
            messages.success(request, f"New Posts successfully added : {added_posts}!!")
            return redirect('posts:index')
    else:
        formset = PostFormSet(queryset=Post.objects.none())
    return render(request, "posts/postformset.html", {'postformset': formset})