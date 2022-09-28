from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


@receiver(post_save, sender=User)
def assign_group(instance: User, created: bool, *args, **kwargs):
    """
    A user is assigned a group (teacher, admin, accountant, etc.)
    for managing permissions. Create the group instance if it does not exist.
    """
    if not created:
        return
    if instance.is_admin:
        instance.groups.add(Group.objects.get_or_create(name="admins")[0])
    if instance.is_teacher:
        instance.groups.add(Group.objects.get_or_create(name="teachers")[0])
    if instance.is_accountant:
        instance.groups.add(Group.objects.get_or_create(name="accountants")[0])
