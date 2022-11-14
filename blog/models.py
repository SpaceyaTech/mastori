from django.db import models
#from django.contrib.auth.models import User

class user(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=45)
    verification_code = models.CharField(unique=True)
    date_created = models.DateField(auto_now_add=True)
    usercol = models.CharField(max_length=45)


    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class account(models.Model):
    id = models.AutoField(primary_key= True, unique=True)
    name = models.CharField(unique=True, max_length=50)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    display_photo = models.ImageField(upload_to="path/to/avatars/", null=True, blank=True)
    bio_data = models.CharField(max_length=1000)

    