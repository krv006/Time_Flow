from django.db.models import Model, DateTime


class TimeBaseModel(Model):
    created_at = DateTime(auto_now_add=True)
    updated_at = DateTime(auto_now=True)