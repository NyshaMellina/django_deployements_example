from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    #create relationship dont inherit from users
    user = models.OneToOneField(User,on_delete=models.PROTECT)

    #Add any additional field
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username