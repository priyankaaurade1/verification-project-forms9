from django.apps import AppConfig


class InvestorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'investor'
    def ready(self):
        import investor.signals
        
