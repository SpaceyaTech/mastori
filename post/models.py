
from operator import mod
from django.db import models
# import uuid
from django.utils.text import slugify
from django.db.models.signals import post_delete,pre_save
from django.dispatch import receiver

from blog.models import Author

# Create your models here.

#handles image location
def upload_location(instance,filename):
    return 'images/{filename}'.format(filename=filename)


class BlogPost(models.Model):
    # uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    body = models.TextField(max_length=5000) 
    image = models.ImageField(upload_to=upload_location,blank=True, null=True) #needs pillow if we go by the picture but if image url will only need a url of the specified image
    date_published = models.DateTimeField(auto_now_add=True,verbose_name ="date published")
    date_updated = models.DateTimeField(auto_now=True,verbose_name ="date updated")
    author = models.ForeignKey(Author,on_delete=models.CASCADE,default=1) 
    #category=models.ForeignKey(Category,on_delete=models.CASCADE) #tied to category model

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-date_published", "-date_updated"]


#when the post is deleted makes sure the image is deleted too
@receiver(post_delete,sender=BlogPost)
def submission_delete(sender,instance,*arg,**kwargs):
    instance.image.delete(False)
