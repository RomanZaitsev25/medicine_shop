from django.apps import AppConfig


class StaffSideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff_side'
    verbose_name = 'Сотрудники аптеки'

    def ready(self):
        import staff_side.signals
