from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    favorite_hero = models.CharField(default = 'None', max_length = 200)
    favorite_antihero = models.CharField(default = 'None', max_length = 200)
    favorite_villian = models.CharField(default = 'None', max_length = 200)
    favorite_team = models.CharField(default = 'None', max_length = 200)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)