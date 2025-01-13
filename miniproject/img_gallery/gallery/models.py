from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
class blogger(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    contact=models.IntegerField()
    def __str__(self):
      return f'name:{self.first_name} age{self.last_name} email{self.email} contact{self.contact}'
class post(models.Model):
    title=models.CharField(max_length=50)
    date=models.IntegerField()
    content=models.CharField(max_length=50)
    blogger=models.ForeignKey('blogger',on_delete=models.CASCADE)
    def __str__(self):
        return f'Title{self.title} date{self.rating} content{self.content}' 