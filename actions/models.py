from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Action(models.Model):
    """
    Model pojedynczej aktywności w strumieniu (odpowiedniku facebookowej tablicy)
    """
    # Użytkownik podejmujący akcję
    user = models.ForeignKey(User, related_name='actions', db_index=True)
    # Opis akcji
    verb = models.CharField(max_length=255)
    # Data wykonania akcji
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    # ContentType określający klasę obiektu, którego dotyczy akcja
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj')
    # ID obiektu, którego dotyczy akcja
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    # Generowany dynamicznie klucz obcy do danego obiektu
    target = GenericForeignKey('target_ct', 'target_id')

    class Meta:
        ordering = ('-created',)
