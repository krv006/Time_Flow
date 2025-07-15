from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('seller', 'Seller'),
        ('user', 'User'),
    )

    username = None
    email = None

    role = CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    phone_number = CharField(max_length=20, unique=True)
    first_name = CharField(max_length=120)
    last_name = CharField(max_length=120)
    date_joined = DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number
