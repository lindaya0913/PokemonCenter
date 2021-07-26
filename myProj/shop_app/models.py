from django.db import models
from django.urls import reverse

class RegisteredUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNum = models.CharField(blank=True, null=True, max_length=20)
    password = models.CharField(max_length=30)
    profilePic = models.ImageField(upload_to='profile_pics', default='default.jpeg')

    def get_absolute_url(self):
        return reverse('userdetail', kwargs = {'pk': self.pk})