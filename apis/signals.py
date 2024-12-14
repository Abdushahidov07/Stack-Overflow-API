import logging
from django.db.models.signals import post_save, post_delete,pre_save
from django.dispatch import receiver
from .models import Questions, Answer

logger = logging.getLogger(__name__)
@receiver(post_save, sender=Questions)
def log_question_creation(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Создан новый вопрос: {instance.title} (ID: {instance.id})")
    else:
        logger.info(f"Вопрос обновлен: {instance.title} (ID: {instance.id})")


@receiver(post_delete, sender=Questions)
def log_question_deletion(sender, instance, **kwargs):
    logger.info(f"Вопрос удалён: {instance.title} (ID: {instance.id})")


@receiver(post_save, sender=Answer)
def log_answer_creation(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Создан новый ответ (ID: {instance.id}) на вопрос ID: {instance.question.id}")



@receiver(pre_save, sender=Questions)
def my_handler(sender, instance, **kwargs):
    print("Hi",instance)
