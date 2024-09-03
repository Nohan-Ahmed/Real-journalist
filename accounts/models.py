from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import Manager
from .utils import COUNTRIES
# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='accounts/media/images', default='static/images/default_avatar.png')
    email = models.EmailField(unique=True, max_length=254)
    date_of_brith = models.DateField()
    bio = models.TextField(null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = Manager()
    
    def __str__(self) -> str:
        return self.username
    
class UserAddress(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='userAddress')
    country = models.CharField(max_length=250, choices=COUNTRIES)
    city = models.CharField(max_length=250)
    zip_code = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=False)