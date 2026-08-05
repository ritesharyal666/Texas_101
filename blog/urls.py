from django.urls import path
from . import views


urlpatterns=[
    path('',views.home_view,name='home'),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact'),
    path('search/',views.search_view,name='search'),
    path('posts/',views.post_list_view,name="post_list"),
    path('posts/<slug:slug>',views.post_detail_view,name="post_detail")
]