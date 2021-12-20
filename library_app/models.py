from django.db import models
from django.urls import reverse
from django.utils import timezone 

# Create your models here.

book_category = (
    ('1', 'Ebook'),
    ('2', 'Hardcopy')
)

book_typ = (
    ('1', 'sports'),
    ('2', 'educational'),
    ('3', 'motivational')
)    



class BOOK(models.Model):
    Book_name = models.CharField(max_length=100)
    Book_description=models.TextField(max_length=250)
    Category=models.CharField(max_length=2, choices=book_category, default=1)
    Publish_Date=models.DateTimeField(default=timezone.now)
    Book_type=models.CharField(max_length=3, choices=book_typ, default=1)
    Price = models.CharField(max_length=50)
    
   
   
    def __str__(self):
        return self.get_category_display()


    def __str__(self):
        return self.Book_name + ' ' + self.Category
    
    def get_absolute_url(self):
        return reverse('app:Book-list')
