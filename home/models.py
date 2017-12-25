from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cul_id = models.AutoField(primary_key=True)
    photo_url = models.URLField(max_length=700, default='', blank=True)
    alt_email = models.EmailField(max_length=100, default='', blank=True)
    college = models.CharField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=100, default='', blank=True)
    year_of_grad = models.CharField(max_length=100, default='', blank=True)
    address = models.CharField(max_length=900, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    state = models.CharField(max_length=100, default='', blank=True)
    serialno = models.CharField(max_length=100, blank=True, default='')
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=1000)
    logout = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    culid = instance.profile.cul_id
    length = len(str(culid))
    if length == 1:
        instance.profile.serialno = "CUL00" + str(culid)
    elif length == 2:
        instance.profile.serialno = "CUL0" + str(culid)
    else:
        instance.profile.serialno = "CUL" + str(culid)
    if instance.profile.rank == 1000:
        instance.profile.rank = sender.objects.count()
    instance.profile.photo_url = 'http://graph.facebook.com/{0}/picture?type=large'.format(instance.username)
    instance.profile.save()


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=855, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(default=timezone.now)
