from django.shortcuts import render
from django.core.mail import send_mail

def index(request): 
	return render(request, 'index.html', {} )

def about(request): 
	return render(request, 'about.html', {} )

def gallery(request): 
	return render(request, 'gallery.html', {} )

def gallerysingle(request): 
	return render(request, 'gallery-single-post.html', {} )

def blog(request): 
	return render(request, 'blog.html', {} )

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


