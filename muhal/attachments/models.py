from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

class Attachment(models.Model):
    label = models.CharField(max_length=100, verbose_name=_('label'))
    file = models.FileField(upload_to='media/', verbose_name=_('file'))
    public = models.BooleanField(default=True, verbose_name=_('public'))

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _('attachment')
        verbose_name_plural = _('attachments')