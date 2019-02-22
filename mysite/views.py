from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	'''username = request.POST.get('nickname','')
	password = request.POST.get('password','')
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			request.session.set_expiry(86400)
			return render(request, 'post_list.html')'''
	return render(request, 'post_list.html')

# Create your views here.

@login_required
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'mysite/post_list.html', {'posts' : posts})

@login_required
def test(request):
	    return render(request, 'mysite/test.html', {})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mysite/post_detail.html', {'post': post})
    
@login_required('')
def new_post(request):
	    return render(request, 'mysite/new_blog_post.html', {})

@login_required('')
def post(request):

    if request.method == 'POST':
        me = User.objects.get(username='mdj')
        title     = request.POST.get('title', '')
        text     = request.POST.get('text', '')
        post_obj = Post(author=me, title=title, text=text)
        post_obj.save()
        post_obj.publish()
    return redirect('post_list')       

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'mysite/signup.html', {'form': form})
    
def logout(request):
    auth.logout(request)
    #return render(request,'login')
    return HttpResponseRedirect('login')
