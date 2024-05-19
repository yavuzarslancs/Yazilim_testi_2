from django.urls import path
from . import views
from app.views import home, home_classic, home_modern, index, blog, blog_single_post, industries, industries_single_industry, not_found_404, register, user_login, logout_view, add_industry, add_blog_post, delete_blog_post, blog_list
from app.views import blog_detail, add_blog_post, delete_blog_post, blog_list, register, user_login, logout_view, add_industry, industry_detail

urlpatterns = [

    path('blog.html', blog_list, name='blog_list'),
    path('blog/add/', add_blog_post, name='add_blog_post'),
    path('blog/delete/<int:pk>/', delete_blog_post, name='delete_blog_post'),
    path('blog/<int:pk>.html', views.blog_detail, name='blog_single'),
    
    path('industries/delete/<int:pk>/', views.delete_industry, name='delete_industry'),

    path('industries/<int:pk>/', views.industry_detail, name='industry_detail'),
    path('industries/<int:pk>/', views.industry_detail, name='industry_detail'),

    path('register.html', register, name='register'),
    path('login.html', user_login, name='login'),
    path('logout/', logout_view, name='logout'),

    path('industries.html', views.list_industries, name='list_industries'),
    path('industries/add/', views.add_industry, name='add_industry'),
    path('blog/add/', views.add_blog_post, name='add_blog_post'),



    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('home-classic.html', views.home_classic, name='home_classic'),
    path('home-modern.html', views.home_modern, name='home_modern'),
    path('', views.home_modern, name='home-modern'),
    path('home-classic.html', views.home, name='home-classic'),
    path('home-modern.html', views.home_modern, name='home-modern'),
    path('index.html', views.index, name='index'),
    path('blog.html', views.blog, name='blog'),
    path('blog-single-post.html', views.blog_single_post, name='blog-single-post'),
    path('industries.html', views.industries, name='industries'),
    path('industries-single-industry.html', views.industries_single_industry, name='industries-single-industry'),
    path('404.html', views.not_found_404, name='404'),
]