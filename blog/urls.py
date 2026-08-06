from django.urls import path
from . import views

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('search/', views.search_view, name='search'),
    path('login/', views.user_login_view, name='login'),
    path('logout/', views.user_logout_view, name='logout'),

    path('post/create/', views.post_create_view, name='post_create'),
    path('post/<slug:slug>/edit/', views.post_edit_view, name='post_edit'),
    path('post/<slug:slug>/delete/', views.post_delete_view, name='post_delete'),
    path('post/<slug:slug>/comment/', views.add_comment_view, name='add_comment'),
    path('post/<slug:slug>/', views.post_detail_view, name='post_detail'),
]