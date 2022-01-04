from django.urls import path
from . import views

urlpatterns = [
	 	path('', views.index, name = "home"),
    	path('index.html', views.index, name = "home"), 
    	path('about.html', views.about, name = "about"), 
    	path('gallery.html', views.gallery, name = "gallery" ), 
    	path('gallery-single-post.html', views.gallerysingle, name = "gallery"), 
    	path('blog.html', views.blog, name = "blog"), 
    	path('blog-single-post.html', views.blogsingle, name = "blogsingle"), 
    	path('contact.html', views.contact, name = "contact"), 
]
