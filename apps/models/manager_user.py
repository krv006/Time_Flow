from django.contrib.auth.hashers import check_password, make_password
from django.db.models import ForeignKey, CASCADE, CharField, Model, DateTimeField


class ManagerUser(Model):
    name = CharField(max_length=100, null=True, blank=True)
    phone_number = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)
    process = ForeignKey('apps.Process', CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk or not ManagerUser.objects.filter(pk=self.pk).exists():
            self.password = make_password(self.password)
        elif not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.phone_number
