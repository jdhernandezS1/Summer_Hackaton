from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configure Challenge application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'challenge'