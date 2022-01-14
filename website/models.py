from django.db import models


class List(models.Model):
	BookName = models.CharField(max_length=200)
	completed = models.BooleanField()
	def __str__(self):
		return self.BookName


class BookList(models.Model):
	book_name = models.CharField(max_length=200)
	book_summary = models.CharField(max_length=50000)
	book_image = models.ImageField(upload_to='images')

	def __str__(self):
		return self.book_name





