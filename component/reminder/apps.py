from django.apps import AppConfig


class ReminderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'component.reminder'

    def ready(self):
        from . import signals