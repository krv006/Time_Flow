from django.db.models import Model, CharField, ForeignKey, CASCADE, OneToOneField


class Product(Model):
    name = CharField(max_length=100)
    process = OneToOneField('apps.Process', CASCADE)

    def __str__(self):
        return self.name


class Process(Model):
    name = CharField(max_length=255)
    manager = ForeignKey('apps.User', CASCADE, limit_choices_to={'role': 'manager'})

    def __str__(self):
        return f"{self.name} -> {self.manager.get_full_name()}"
