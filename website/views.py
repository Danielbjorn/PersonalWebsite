from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import List
from .models import BooksList
from .forms import ListForm
from .forms import BookForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request): 
	return render(request, 'index.html', {} )

def about(request): 
	return render(request, 'about.html', {} )

def addbook(request):
	

	if request.method == 'POST':
		bookform = BookForm(request.POST, request.FILES)
		
		if bookform.is_valid():
			bookform.save()
			book_obj = bookform.instance
			return render(request, 'addbook.html', {'bookform': bookform, 'book_obj': book_obj})

	else:
		bookform = BookForm()

	return render(request, 'addbook.html', {'bookform': bookform})



	











def books_single(request): 
	return render(request, 'books_single_post.html', {} )

def books(request):
	all_items = List.objects.all
	return render(request, 'books.html', {'all_items': all_items} )

def reports(request): 
	return render(request, 'reports.html', {} )

def blogsingle(request): 
	return render(request, 'blog-single-post.html', {} )

def contact(request): 

	if request.method == "POST":

		fname = request.POST['fname']
		address = request.POST['address']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		send = request.POST['send']

		#Send email
		send_mail(
			fname,	
			message,
			fname,
			['danielbjorn94@gmail.com'],
			fail_silently=False,
			)

		return render(request, 'contact.html', {'fname': fname} )

	else: 
		return render(request, 'contact.html', {} )


def delete(request, list_id): 
	BookName = List.objects.get(pk=list_id)
	BookName.delete()
	messages.success(request, ('Book Has Been Removed From Database!'))
	return redirect('books')