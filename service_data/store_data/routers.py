from store_data.models import UserWeight

ROUTED_MODELS = [UserWeight]


class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'userweight'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'userweight'
        return None
