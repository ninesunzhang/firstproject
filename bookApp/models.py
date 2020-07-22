from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    def __repr__(self):
        return '<Book: %s>' %(self.title)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "books"
        verbose_name="tushuguanli"
        verbose_name_plural="tushuguanli"

class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=20)
    Book = models.ForeignKey('Book',on_delete=models.CASCADE)

    def __repr__(self):
        return '<Hero: %s>' %(self.title)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "heros"
        verbose_name="renwuguanli"
        verbose_name_plural="renwuguanli"
