from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()

    def __str__(self):
        return  "Book: %d" %(self.name)
    class Meta:
        db_table = "books"

class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=20)
    Book = models.ForeignKey('Book',on_delete=models.CASCADE)

    def __str__(self):
        return "Hero: %s" % (self.name)

