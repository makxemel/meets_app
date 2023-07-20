from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from .services import watermark_avatar_service


def image_directory_path(instance, filename):
    return f'media/{instance}/{filename}'


class User(AbstractBaseUser, PermissionsMixin):
    genders = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    avatar = models.ImageField(upload_to=image_directory_path, blank=True)
    gender = models.CharField(max_length=6, choices=genders)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_first_name(self):
        return self.first_name


class Likes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user')
    user_like = models.ManyToManyField(User, related_name='user_like', blank=True)


@receiver(post_save, sender=User)
def after_user_was_created(sender, instance, created, **kwargs):
    if created:
        watermark_avatar_service(instance.avatar.path)
        Likes.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user(sender, instance, **kwargs):
#     pass





