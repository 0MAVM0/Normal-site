from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    interests = models.TextField(max_length=255)
    last_visit = models.DateTimeField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.profile_image:
            try:
                img = Image.open(self.profile_image.path)

                if img.height > 100 or img.width > 100:
                    output_size = (100, 100)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
            except (FileNotFoundError, ValidationError) as e:
                print(f"Error processing profile image: {e}")
