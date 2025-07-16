from django.db.models import Model, CharField, ForeignKey, CASCADE


class Process(Model):
    name = CharField(max_length=255)
    user = ForeignKey('apps.User', CASCADE, limit_choices_to={'role': 'manager'})

    def __str__(self):
        return f"{self.name} -> {self.user.get_full_name()}"
