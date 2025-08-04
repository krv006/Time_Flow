from django.db.models import CharField, ForeignKey, CASCADE, DateField, Model, DateTimeField
from django.utils import timezone

from apps.models import TimeBaseModel


class Material(TimeBaseModel):
    name = CharField(max_length=120)


class Processing(Model):
    Action_type = (
        ('Kirim', 'kirim'),
        ('Chiqim', 'chiqim'),
    )

    processing = CharField(max_length=120, choices=Action_type)
    data = DateField(default=timezone.now)
    created_at = DateTimeField(auto_now_add=True)
    material = ForeignKey('apps.Material', CASCADE, related_name='processing')
    user = ForeignKey('apps.User', CASCADE, related_name='processing', limit_choices_to={'role': 'warehouseman'})
