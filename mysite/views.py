from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'mysite/post_list.html', {'posts' : posts})

def test(request):
	    return render(request, 'mysite/test.html', {})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mysite/post_detail.html', {'post': post})

def new_post(request):
	    return render(request, 'mysite/new_blog_post.html', {})
