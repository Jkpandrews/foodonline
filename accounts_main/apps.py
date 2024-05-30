from django.apps import AppConfig


class AccountsMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts_main'

    def ready(self):
        import accounts_main.singnals