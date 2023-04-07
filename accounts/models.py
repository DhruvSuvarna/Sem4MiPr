from django.db import models

# from django.contrib.auth.models import User #, AbstractBaseUser, PermissionsMixin, UserManager
# from django.core.validators import RegexValidator
# from django.utils import timezone

from django.contrib.auth.models import AbstractUser #, BaseUserManager
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('donor', 'Donor'),
        ('orphanage', 'Orphanage'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')
    class Meta:
        db_table = 'auth_user'

'''
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        DONOR = "DONOR", "Donor"
        ORPHANAGE = "ORPHANAGE", "Orphanage"

    base_role = Role.DONOR

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class DonorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.DONOR)


class Donor(User):

    base_role = User.Role.DONOR

    student = DonorManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for donors"


@receiver(post_save, sender=Donor)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "DONOR":
        DonorProfile.objects.create(user=instance)


class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    donor_id = models.IntegerField(null=True, blank=True)


class OrphanageManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ORPHANAGE)


class Orphanage(User):

    base_role = User.Role.ORPHANAGE

    orphanage = OrphanageManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for orphanages"


class OrphanageProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orphanage_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Orphanage)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "ORPHANAGE":
        OrphanageProfile.objects.create(user=instance)
'''
'''
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email= email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin): 
    email= models.EmailField(blank=True, defaut='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]

'''