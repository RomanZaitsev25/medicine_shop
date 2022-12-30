from django.apps import AppConfig


class ClientSideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'client_side'
    verbose_name = 'Сайт для клиента'

    def ready(self):
        import client_side.signals
