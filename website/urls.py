from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	 	path('', views.index, name = "home"),
    	path('index.html', views.index, name = "home"), 
    	path('about.html', views.about, name = "about"),
    	path('addbook.html', views.addbook, name ="addbook"), 
    	path('books.html', views.books, name = "books" ), 
    	path('books_single_post.html', views.books_single, name = "books_single"), 
    	path('reports.html', views.reports, name = "reports"), 
    	path('blog-single-post.html', views.blogsingle, name = "blogsingle"), 
    	path('contact.html', views.contact, name = "contact"), 
        path('upload/', views.addbook, name = "addbook"),

    	path('delete/<list_id>', views.delete, name='delete'),
        path('show_book/<book_id>', views.show_book, name = "show-book"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
