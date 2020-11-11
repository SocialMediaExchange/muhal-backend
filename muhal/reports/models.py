import os

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers
from django.utils.translation import gettext_lazy as _

from cases.models import COUNTRY_CHOICES

class Report(models.Model):
    submitter = models.CharField(max_length=100, null=True, verbose_name=_('submitted by'))
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, verbose_name=_('country'))
    plaintiff = models.CharField(max_length=200, verbose_name=_('plaintiff'))
    defendant = models.CharField(max_length=200, verbose_name=_('defendant'))
    what_happened = models.TextField(verbose_name=_('What happened'))
    
    notes = models.TextField(blank=True, null=True, verbose_name=_('Our notes'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    last_modified = models.DateTimeField(auto_now=True, verbose_name=_('Last modified'))
    processed = models.BooleanField(default=False, verbose_name=_('Processed?'))

    def __str__(self):
        return self.what_happened[:20]

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')


@receiver(post_save, sender=Report)
def notify_admins(sender, instance, **kwargs):
    if kwargs['created']: 
        subject = 'إبلاغ جديد'
        message = f'New report! To view, go to http://{os.environ["PROJECT_URL"]}/admin/reports/report/{instance.id}/change/'
        html_message = f'<div dir="rtl">\
        مرحبا، \
        <br/ >\
        وصلنا إبلاغ جديد عن حالة جديدة. التفاصيل أدناه: \
        <br/ >\
        <b>الدولة</b>: {instance.country} \
        <br/ >\
        <b>الجهة المدعية</b>: {instance.plaintiff} \
        <br/ >\
        <b>الجهة المدعى عليها</b>: {instance.defendant} \
        <br/ >\
        <b>ما الذي حصل؟</b>: \
        <br/ >\
        {instance.what_happened} \
        <br/ >\
        <a href="http://{os.environ["PROJECT_URL"]}/admin/reports/report/{instance.id}/change/">لعرض الإبلاغ</a>\
        <br/ >\
        http://{os.environ["PROJECT_URL"]}/admin/reports/report/{instance.id}/change/ \
        <br/ >\
        </div>'
        mail_managers(subject, message=message, html_message=html_message)