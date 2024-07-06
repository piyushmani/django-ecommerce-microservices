from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class AbstractBaseUser(AbstractUser):
    # Just use for User model
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.IntegerField(null=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    updated_by = models.IntegerField(null=True)

    is_deleted = models.BooleanField(default=True)

    deleted_at = models.DateTimeField(default=None, null=True)
    deleted_by = models.IntegerField(null=True)
    

    objects = UserManager()
    class Meta: 
        abstract = True

class User(AbstractBaseUser):
    
    """User Model"""

    gender_choice = (
        ("M", "Male"),
        ("F", "Female"),
        ("Other", "Other"),

    )
    status_choice = (
        ("Active", "Active"),
        ("Deleted", "Deleted"),

        ("suspended", "suspended"),
        ("Blocked", "Blocked"),
        ("restricted", "restricted"),

    )
    first_name = models.CharField(
        max_length=100, null=True, verbose_name='First Name', help_text='First name of  user')
    last_name = models.CharField(
        max_length=100, null=True, verbose_name='Last Name', help_text='Last name of  user')
    email = models.EmailField(max_length=100, unique=True,
                            verbose_name='User email', help_text='Email of  user')
    phone_number = models.CharField(
        max_length=50, unique=False, null=True, verbose_name='Phone user', help_text='Phone of user')
    gender = models.CharField(max_length=100, null=True, choices=gender_choice,
                            verbose_name='User sex', help_text='Sex of User')
    bvn = models.CharField(max_length=100, null=True, verbose_name='BVN')
    birthday = models.DateField(null=True,
        verbose_name='Birthday', help_text='Birthday of user')
    status = models.CharField(max_length=100, choices=status_choice, default='Active',
                            verbose_name='User status', help_text='User status')

    last_login = models.DateTimeField(
        verbose_name='Last login', help_text='Last login', auto_now_add=True)

    class Meta:
        """Metadata"""
        ordering = ["first_name", "last_name"]

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'