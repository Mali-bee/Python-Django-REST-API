from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)         #get user input of name and convert data type to String
    age = models.IntegerField()                     #get user input of age and convert data type to Interger
    
    def __str__(self):
        return self.name                            #to print for error handling
    