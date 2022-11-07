
from django.db import models
import uuid
from django.db.models.signals import post_delete
from django.dispatch import receiver

from blog.models import Author

# Create your models here.

#handles image location
def upload_location(instance,filename):
    file_path='blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id),
        title=str(instance.title),
        filename=filename
    )
    return file_path


class BlogPost(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=50, null=False,blank=False)
    description = models.CharField(max_length=300,null=False,blank=False)
    body = models.TextField(max_length=5000,null=False,blank=False) 
    image = models.ImageField(upload_to=upload_location,null=False,blank=False) #needs pillow if we go by the picture but if image url will only need a url of the specified image
    date_published = models.DateTimeField(auto_now_add=True,verbose_name ="date published")
    date_updated = models.DateTimeField(auto_now=True,verbose_name ="date updated")
    date_deleted = models.DateTimeField(auto_now =True,verbose_name ="date deleted")
    author = models.ForeignKey(Author,on_delete=models.CASCADE,default=1) 
    #slug = models.SlugField()
    #category=models.ForeignKey(Category,on_delete=models.CASCADE) #tied to category model

    def __str__(self) -> str:
        return self.title

#when the post is deleted makes sure the image is deleted too
@receiver(post_delete,sender=BlogPost)
def submission_delete(sender,instance,*arg,**kwargs):
    instance.image.delete(False)

# #slugs are unique
# def pre_save_post_receiver(sender, instance,*args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.author.username+ "-"+instance.title)

# pre_save.connect(pre_save_post_receiver, sender=BlogPost)