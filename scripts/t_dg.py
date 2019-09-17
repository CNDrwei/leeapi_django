import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.dev')
django.setup()


from django.conf import settings
# <Settings "luffyapi.settings.dev">
print(settings)


# import logging
# # from logging import config
# # config.dictConfig(settings.LOGGING)
# logger = logging.getLogger('django')
# logger.debug('debug')
# logger.info('info')

# from utils.logging import logger
# logger.debug('111111111111111')

from apps.user import models
print(models)




