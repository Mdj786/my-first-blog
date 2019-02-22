from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout



urlpatterns = [
	#path('', auth_views.login, {'template_name': 'mysite/login.html'}, name='login'),
    #path('post_list/', views.post_list, name='post_list'),
    
    path('login', auth_views.login, {'template_name': 'mysite/login.html'}, name='login'),
    path('', views.post_list, name='post_list'),
    
    
    
    
    
    #path('post_list/', login_required(views.post_list), name='post_list'),
    #path('', views.test, name='new_page'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('new_post/', views.new_post, name='new_post'),
    path('post/', views.post, name='post'),
    
    path('signup/',views.signup, name='signup'),
    
    

    path('logout/', logout, {'next_page': 'login'}, name='logout')
    


    
]
