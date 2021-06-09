from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse




#User = get_user_model()


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_marketing = models.BooleanField(default=False)


    class Meta:
        swappable = 'AUTH_USER_MODEL'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    cover = models.ImageField(upload_to='bookapp/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)        


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.message)

class BookReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.IntegerField(max_length=100)
    genre = models.CharField(max_length=100)
    reservation_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user,self.book_id, self.genre, self.reservation_date)

    def raport(self,genre):
        l = BookReservation.objects.filter(genre = genre).count()
        return l

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)


class DeleteRequest(models.Model):
    delete_request = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.delete_request

class UserDeleteRequest(models.Model):
    user_delete_request = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.user_delete_request


class Feedback(models.Model):
    feedback = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.feedback












