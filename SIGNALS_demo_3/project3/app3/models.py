
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        logger.info("Signal handler is in the same transaction.")
    else:
        logger.info("Signal handler is not in the same transaction.")
