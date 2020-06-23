from django.db import models  
  
  
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    
    def __str__(self):
	    return self.full_name

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
	    return self.name
        
class Friend(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
	    return self.name
    
class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    copy_count = models.SmallIntegerField(default=1)  
    price = models.DecimalField(max_digits=12, decimal_places=2)  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, null=True, blank=True, related_name='books')   
    img = models.ImageField(upload_to='media', blank=True)
    def __str__(self):
	    return self.title
        
