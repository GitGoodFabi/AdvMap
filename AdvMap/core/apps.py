from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

class InstaRouter:
    route_app_labels = {'core'}  # oder dein App-Name

    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'insta_routes':
            return 'insta'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'insta_routes':
            return 'insta'
        return None
