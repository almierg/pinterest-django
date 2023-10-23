from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse


class İmage(models.Model):
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    title=models.CharField(max_length=200)
    body=RichTextField(null=True,blank=True)
    user=models.ForeignKey( User,on_delete=models.CASCADE)
    category=models.CharField(max_length=200)
    post_date=models.DateField(blank=True, null=True,auto_now_add=True)
    snippet=models.CharField(blank=True, null=True,max_length=250)
    likes=models.ManyToManyField(User, related_name='like')

    def total_likes(self):
       return self.likes.count()
    
    def __str__(self):
        return self.title
    

class Profile(models.Model):
    profil_pic=models.ImageField(null=True, blank=True, upload_to="images/profile/")
    user=models.ForeignKey( User, null=True, on_delete=models.CASCADE)
    e_posta=models.EmailField(max_length=250)
    bio=models.TextField(null=True, blank=True)
    follower=models.ManyToManyField(User,related_name='follower',null=True, blank=True)

    def __str__(self):
        return str(self.user)   

class Pin(models.Model):
    pin_title=models.CharField(max_length=200)
    pin_body=RichTextField(null=True,blank=True)
    url=models.CharField(max_length=200)
    pin_image=models.ImageField(null=True, blank=True, upload_to="images/pin_photo/")

class Pano(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class Comment(models.Model):
    name=models.CharField(max_length=250)
    body=models.TextField(max_length=250)
    post=models.ForeignKey(İmage,null=True,related_name="comments",on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return '%s - %s' % (self.post.title ,self.name)

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField(max_length=250)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.user, self.body