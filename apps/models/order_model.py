from django.db.models import ForeignKey, CASCADE, CharField

from apps.models import TimeBaseModel


class ManagerUser(TimeBaseModel):
    name = CharField(max_length=100, null=True, blank=True)
    phone_number = CharField(max_length=255)
    password = CharField(max_length=255)
    process = ForeignKey('apps.Process', CASCADE)
