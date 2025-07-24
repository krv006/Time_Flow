from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, ForeignKey, DateTimeField, BooleanField, CharField
from django.utils import timezone

from apps.models import CustomUserManager


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('seller', 'Seller'),
        ('user', 'User'),
    )

    username = None
    email = None

    phone_number = CharField(max_length=20, unique=True)
    first_name = CharField(max_length=120)
    last_name = CharField(max_length=120)
    role = CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    date_joined = DateTimeField(default=timezone.now)

    # todo ManagerUser'dan qo‘shilganlar
    process = ForeignKey('apps.Process', CASCADE, related_name='users', null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    is_active = BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
