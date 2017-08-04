from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    """
    Model rozszerzający model django.contrib.auth.model.User
    """
    user=models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth=models.DateField(blank=True, null=True)
    photo=models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return "Profil użytkownika {}.".format(self.user.username)