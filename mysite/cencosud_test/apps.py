from django.apps import AppConfig


class CencosudTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cencosud_test'

    # def ready(self):
    #         print('Starting Scheduler')
    #         from .scheduler import weather_scheduler
    #         weather_scheduler.start()

