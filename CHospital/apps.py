from django.apps import AppConfig


class ChospitalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CHospital'

    def ready(self):
        import CHospital.signals