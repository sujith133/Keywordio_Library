
from pyexpat import model
from django.db import models

class logins(models.Model):
    username=models.CharField(max_length=150)
    useremail=models.EmailField(max_length=100)
    password=models.CharField(max_length=100,)

    def __str__(self):
        return self.username+" "+self.useremail+" "+self.password


class book(models.Model):
    BookId=models.IntegerField(primary_key=True)
    BookName=models.CharField(max_length=100)
    BookStatus=models.CharField(max_length=100)

    def __str__(self):
        return self.BookId+"    "+self.BookName+"    "+self.BookStatus