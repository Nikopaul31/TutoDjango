from django.db import models
from datetime import timezone
import django.utils.timezone

class Device(models.Model):
    IOS = 'ios'
    ANDROID = 'android'
    TABLET = 'tablet'
    PHONE = 'phone'

    OS_LIST = [
        (IOS, 'ios'),
        (ANDROID, 'android')
    ]

    PLATFORM_CHOICES = [
        (TABLET, 'tablet'),
        (PHONE, 'phone')
    ]

    os = models.CharField(max_length=20, choices=OS_LIST, default='non defini')
    form_platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default='non defini')
    model = models.CharField(max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, default='')
    enabled = models.BooleanField(default=True)

    def __str__(self,):
        return """
        device ID : {},
        os : {},
        form_platform : {},
        model {},
        created_at {},
        description {},
        enabled {},
        """.format(self.pk, self.os, self.form_platform, self.model, self.created_at, self.description, self.enabled)
