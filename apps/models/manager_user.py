from django.contrib.auth.hashers import make_password
from django.db.models import ForeignKey, CASCADE, CharField, Model, DateTimeField


class ManagerUser(Model):
    name = CharField(max_length=100, null=True, blank=True)
    phone_number = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)
    process = ForeignKey('apps.Process', CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # todo Password hash
        if not self.pk or 'password' in self.get_dirty_fields():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number
