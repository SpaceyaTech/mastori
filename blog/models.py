from django.db import models
# note that im useing the Django inbuild user model
class account(models.Model):
    id = models.AutoField(primary_key= True, unique=True)
    name = models.CharField(unique=True, max_length=50)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    display_photo = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    bio_data = models.CharField(max_length=1000)
    """
    note the user is from django builtin user model
    i'm using foreignkey which allows one user to have many account
"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class blogposts(models.Model):
    id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=500)
    blog_description = models.TextField()
    content = models.TextField
    blogpostscol = models.CharField(max_length=45)
    account_name = models.ForeignKey('account.name',on_delete=models.CASCADE)