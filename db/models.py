import binascii
import os

from django.db import models
from model_utils.models import TimeStampedModel


class User(models.Model):
    """
    Just example model for development, it will be updated soon
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class AuthToken(TimeStampedModel):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(User, related_name='auth_token', on_delete=models.CASCADE)

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = binascii.hexlify(os.urandom(20)).decode()
        return super().save(*args, **kwargs)


class Category(TimeStampedModel):
    title = models.CharField(max_length=64)
    url = models.SlugField(allow_unicode=True)
    owners = models.ManyToManyField(User, related_name='categories')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class InfoObject(TimeStampedModel):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    big_image = models.ImageField(upload_to='info_objects/big', blank=True, null=True)
    small_image = models.ImageField(upload_to='info_objects/small', blank=True, null=True)
    owners = models.ManyToManyField(User, related_name='info_objects')

    def __str__(self):
        return self.title


class Feedback(TimeStampedModel):
    subject = models.CharField(max_length=256)
    text = models.TextField(blank=True)

    def __str__(self):
        clean_words = [word for word in self.subject.split() if word]
        return ' '.join([word for word in clean_words][:5]) + '...' if len(clean_words) > 5 else ''
