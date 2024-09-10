from django.apps import AppConfig

class HappyperformerbackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'happyPerformerBackend'

    def ready(self):
        # Import the signals module to ensure it's loaded when the app is ready
        import happyPerformerBackend.signals
