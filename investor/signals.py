from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Document
from Crypto.Cipher import AES
import os,traceback

@receiver(pre_save, sender=Document)
def encrypt_DocumentData(sender, instance, **kwargs):
    try:
        if not instance.pk:
            key = os.urandom(32)
            iv = os.urandom(16)
            cipher = AES.new(key, AES.MODE_GCM, iv)
            ct, tag = cipher.encrypt_and_digest(instance.image)
            instance.key = key
            instance.iv = iv
            instance.tag = tag
            instance.image = ct
    except Exception as e:
        print(traceback.format_exc())
        pass

