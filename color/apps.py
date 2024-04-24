from django.apps import AppConfig


class ColorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'color'

    def ready(self):
        import color.signals  # noqa