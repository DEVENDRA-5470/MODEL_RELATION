from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    ############################### one to one realationship betweent two tables ##############################
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    profile_img =  models.ImageField(default = 'media/default.jpg', upload_to = 'pics', null = True, blank = True)

    name = models.CharField(default = 'Hey , (Default)', max_length=200, null=True)

    title = models.CharField(default = 'This is the default, title change it in profile.', max_length=200, null=True)

    desc_text = 'Hey, there this is a default text description about you that you can change on after clicking on "Edit" or going to your profile page.'

    desc = models.CharField(default = desc_text, max_length=200, null=True)

    links="Profile Link"
    instagram=models.URLField(null=True , default=links)
    github=models.URLField(null=True , default=links)
    linkedin=models.URLField(null=True , default=links)


    def __str__(self):
        return f'{self.user.username} Profile'


################################ Many to one ########################################## 
class Author(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=40)

    def __str__(self):
        return self.firstName + self.lastName
    
class Book(models.Model):
    title = models.CharField(max_length=150)
    published_date = models.DateField()
    content=models.TextField()

    author = models.ManyToManyField('Author', related_name='books')
    
    class Meta:
        ordering = ['-published_date']
        
    
    # Create your models here.

class Comment(models.Model):
    text = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book, related_name='comments')
    def __str__(self):
        return f"Comment by {self.user.username}: {self.text[:20]}"

        
