from django.shortcuts import render, reverse, HttpResponseRedirect
from ghost_post.models import Post
from ghost_post.forms import PostForm
# Create your views here.
def index(request):
    html = 'index.html'
    posts = Post.objects.order_by('-date')
    return render(request, html, {"posts":posts})

def score(request):
    html = 'index.html'
    posts = sorted(Post.objects.all(), key=lambda post: (post.upVotes - post.downVotes))
    posts.reverse()
    return render(request, html, {"posts":posts})

def boasts(request):
    html = 'index.html'
    posts = Post.objects.filter(isBoast=True).order_by('-date')
    return render(request, html, {"posts":posts})

def roasts(request):
    html = 'index.html'
    posts = Post.objects.filter(isBoast=False).order_by('-date')
    return render(request, html, {"posts":posts})

def new_post_form(request):
    html = 'genericform.html'
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                isBoast=data['post_type'],
                content=data['post'],
                upVotes=0,
                downVotes=0
            )
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage'))
            )
    
    form = PostForm()
    return render(request, html, {'form': form})

def post(request, id):
    html = "post.html"
    post = Post.objects.get(id=id)
    next_post = post.id + 1 if post.id < Post.objects.last().id else False
    last_post = post.id - 1 if post.id > Post.objects.first().id else False
    return render(request, html, {
        "post":post,
        "homepage":reverse('homepage'),
        "next_post":next_post,
        "last_post":last_post
        })

def upVote(request, id):
    post = Post.objects.get(id=id)
    post.upVotes += 1
    post.save()
    return HttpResponseRedirect(reverse("post", kwargs={"id":id}))

def downVote(request, id):
    post = Post.objects.get(id=id)
    post.downVotes += 1
    post.save()
    return HttpResponseRedirect(reverse("post", kwargs={"id":id}))