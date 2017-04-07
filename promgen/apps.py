import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class PromgenConfig(AppConfig):
    name = 'promgen'

    def ready(self):
        from promgen import signals  # NOQA