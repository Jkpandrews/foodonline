from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import UserProfile,User


@receiver(post_save, sender= User)
def postSaveCreateProfileReceiver(sender, instance, created, **kwargs)  :
    if created:
        UserProfile.objects.create( user=instance)
        print('user created')
    else:
        #create user profile if not exist
        UserProfile.objects.get(user=instance)
        print('profile was not exist, but i created one')
    print('user is updated')

@receiver(pre_save, sender= User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'this user is being saved')

# post_save.connect(postSaveCreateProfileReceiver, sender=User)