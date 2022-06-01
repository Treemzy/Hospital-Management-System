from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=100, null=True, blank=True, default=None)
    creator = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.role

    def get_absolute_url(self):
        return reverse('CHMS-Role')


class User(AbstractUser):
    is_admin = models.BooleanField('Admin', default=False)
    is_superadmin = models.BooleanField('Super Admin', default=False)
    roles = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('CHMS-AllUsers')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField('Active', default=False)
    bio = models.CharField(max_length=100, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)