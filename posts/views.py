from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Post
from .forms import BlogPostForm
from .forms import PostSearchForm
from django.db.models import Q

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    search_form = PostSearchForm()
    return render(request, "posts/posts_list.html", {'posts': posts, 'search_form': search_form})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    
    can_edit = request.user == post.author or request.user.is_superuser
    does_like = request.user.profile in post.liked_by.all()
    
    return render(request, "posts/post_detail.html", {'post': post, 'can_edit': can_edit, 'does_like': does_like})

def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("posts_list")  
        else:
            return render(request, "posts/post_form.html", {"form": form})
    else:
        form = BlogPostForm()
        return render(request, "posts/post_form.html", {"form": form})



def edit_post(request, id):
    # Load the post we're changing, from the DB
    post = get_object_or_404(Post, pk=id)

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        return update_post(form)
    else:
        form = BlogPostForm(instance=post)
        return render(request, "posts/post_form.html", {"form": form})
    
    
def update_post(form):
    # Update the DB with the differences
    if form.is_valid():
        post = form.save()
        return redirect("post_detail", id=post.id) 
    else:
         return render(request, "posts/post_form.html", {"form": form})


def like_post(request, id):
    post = get_object_or_404(Post, pk=id)
    request.user.profile.likes.add(post)
    return redirect("post_detail", id=post.id)


def unlike_post(request, id):
    post = get_object_or_404(Post, pk=id)
    request.user.profile.likes.remove(post)
    return redirect("post_detail", id=post.id)



def search_posts(request):
    query = request.GET['q']
    
    query_by_title = Q(title__contains=query)
    query_by_content = Q(content__contains=query)
    posts = Post.objects.filter(query_by_title | query_by_content)
    
    return render(request, "posts/posts_list.html", {'posts': posts})
    

def filter_post_list(request):


    posts = Post.objects.all()
    
    if 'search' in request.GET:
        search = request.GET['search']
        
        query_by_naamdier = Q(naamdier__contains=search)
        query_by_kortebeschrijving = Q(kortebeschrijving__contains=search)

        posts = posts.filter(query_by_naamdier | query_by_kortebeschrijving)

    
    if request.GET['soort'] != 'X':
        posts = posts.filter(soort=request.GET['soort'])

    

    search_form = PostSearchForm(request.GET)
    return render(request, "posts/posts_list.html", {'posts': posts, 'search_form': search_form})
    
    