from django.db import models

# Create your models here.

class chapters(models.Model):
    chapter = models.IntegerField()
    datecreated = models.IntegerField()
    createdby = models.CharField(max_length=255)


    def __str__(self):
        return f"The chapter #{self.chapter} was created on {self.datecreated} by {self.createdby}"



class bookstore(models.Model):
    bookname = models.CharField(max_length=255)
    published = models.IntegerField(max_length=4)
    author = models.CharField(max_length=255)
    information = models.CharField(max_length=855)
    yearwritten = models.IntegerField(max_length=4)
   


    def __str__(self):
        return f"The {self.bookname} book was written in the year of {self.yearwritten} by {self.author} and was published on {self.published} with the description of {self.information}"
