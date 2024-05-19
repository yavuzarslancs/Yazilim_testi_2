from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from .models import Industry, BlogPost
from .forms import IndustryForm, BlogPostForm

from django.contrib.auth import logout as auth_logout


from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

from django.contrib.auth.decorators import login_required


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog-single-post.html', {'post': post})

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

@login_required
def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'add_blog_post.html', {'form': form})
    
@login_required
def delete_blog_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return redirect('blog_list')

def list_industries(request):
    industries = Industry.objects.all()
    return render(request, 'industries.html', {'industries': industries})


@login_required
def delete_industry(request, pk):
    industry = get_object_or_404(Industry, pk=pk)
    industry.delete()
    return redirect('list_industries')

@login_required
def add_industry(request):
    if request.method == 'POST':
        form = IndustryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_industries')
    else:
        form = IndustryForm()
    return render(request, 'add_industries.html', {'form': form})

def industry_detail(request, pk):
    industry = get_object_or_404(Industry, pk=pk)
    return render(request, 'industries-single-industry.html', {'industry': industry})



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'registration_success.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login_succes.html')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı.')
    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('index')



def home(request):
    return render(request, 'home-modern.html')

def home_classic(request):
    return render(request, 'home-classic.html')

def home_modern(request):    
    return render(request, 'home-modern.html')

def home_modern(request):
    """ Görünüm fonksiyonu modern ana sayfa için """
    return render(request, 'home-modern.html')

def home_classic(request):
    """ Görünüm fonksiyonu klasik ana sayfa için """
    return render(request, 'home-classic.html')

def index(request):
    """ Görünüm fonksiyonu indeks sayfası için """
    return render(request, 'index.html')

def blog(request):
    """ Görünüm fonksiyonu blog listesi için """
    return render(request, 'blog.html')

def blog_single_post(request):
    """ Görünüm fonksiyonu tekil blog yazısı için """
    return render(request, 'blog-single-post.html')

def industries(request):
    """ Görünüm fonksiyonu endüstri listesi için """
    return render(request, 'industries.html')

def industries_single_industry(request):
    """ Görünüm fonksiyonu tekil endüstri sayfası için """
    return render(request, 'industries-single-industry.html')

def not_found_404(request):
    """ Görünüm fonksiyonu 404 hata sayfası için """
    return render(request, '404.html')
