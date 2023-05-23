import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse

from accounts.models import Account

from .utils import unique_slug_generator


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Category

class Category(AbstractBaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

"""stori is swahili for story. was thinking of using the slang version 'risto'/'riba' in there.. """
class Stori(AbstractBaseModel):
    class Status(models.TextChoices):
        Draft = "Draft"
        Published = "Published"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    content = RichTextUploadingField()
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=9,choices=Status.choices, default=Status.Draft) #"""This here serves to indicate whether a stori has been published or not."""
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    

    def __str__(self):
         return f'{self.title} created by: {self.created_by}'
         
    class Meta:
        verbose_name_plural = "Mastori"

    def get_absolute_url(self):
        return reverse("blog-detail",kwargs={"pk":self.id})


@receiver(pre_save, sender=Stori)
def auto_slug(sender, instance, **kwargs):
    """Auto populates slug from title for the Stori model"""
    instance.slug = unique_slug_generator(instance)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    stori = models.ForeignKey(Stori,on_delete= models.CASCADE,related_name="comment")
    account = models.ForeignKey(Account, on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    reactions = models.PositiveIntegerField(default=0)
    #make the initial comment parent
    parent_comment = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='replies')
    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.account.account_name) 
    
    def child_comment(self):#get all child comments
        return Comment.objects.filter(parent_comment=self)
    
    @property #make comment a parent if it gets a reply 
    def is_parent(self):
        if self.parent_comment is not None:
            return False
        return True
    def get_absolute_url(self):
        return reverse("comments-detail",kwargs={"pk":self.id})

REACTION_TYPE_CHOICES = (
    ('Like', 'Like'),
    ('Dislike', 'Dislike')
)

class Reaction(AbstractBaseModel):
    reaction_type = models.CharField(max_length=100, choices=REACTION_TYPE_CHOICES)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Stori, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.reaction_type