from django.db import models
from accounts.models import Account
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Category
class Category(AbstractBaseModel):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

""" Stori """
""" stori_status """
STATUS = (
    (0,"Draft"),
    (1,"Published")
)
"""stori is swahili for story. was thinking of using the slang version 'risto'/'riba' in there.. """
class Stori(AbstractBaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    content = RichTextUploadingField()
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=STATUS, default=0) #"""This here serves to indicate whether a stori has been published or not."""
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    

    def __str__(self):
         return f'{self.title} created by: {self.created_by}'
         
    class Meta:
        verbose_name_plural = "Mastori"
        
@receiver(pre_save,sender=Stori) #auto populates slug from title for the Stori model
def auto_slug(sender,instance, **kwargs):
    instance.slug = slugify(instance.title)
pre_save.connect(auto_slug,sender=Stori)


class Comment(models.Model):
    body = models.TextField()
    Post_id = models.ForeignKey(Stori,on_delete= models.CASCADE)
    user = models.ForeignKey(Account, on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    reactions = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.user.name)

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