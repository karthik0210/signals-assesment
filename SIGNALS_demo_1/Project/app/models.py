from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
import time

logger = logging.getLogger(__name__)

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    start_time = time.time()
    logger.info(f"Signal handler started at {start_time}")
    # Simulate a delay
    time.sleep(10)
    end_time = time.time()
    logger.info(f"Signal handler ended at {end_time}")

