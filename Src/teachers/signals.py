from django.db.models.signals import pre_save
from django.dispatch import receiver
from teachers.models import Teacher


@receiver(pre_save, sender=Teacher)
def pre_save_teacher(sender, instance, **kwargs):
    instance.email = instance.email.lower()
    instance.telephone = ''.join(i for i in instance.telephone if i.isdigit())
    instance.first_name = instance.first_name.title()
    instance.last_name = instance.last_name.title()

    if instance.id is None:
        print('Object is created!')