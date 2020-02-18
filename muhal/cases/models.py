from django.db import models
from mezzanine.core.models import Displayable
from django.utils.translation import gettext_lazy as _

GENDER_CHOICES = [
    ('male', _('Male')),
    ('female', _('Female')),
    ('other', _('Other')),
]

CITIZENSHIP_CHOICES = [
    ('leb', _('Lebanese')),
    ('syr', _('Syrian')),
    ('non', _('Stateless')),
    ('other', _('Other')),
]

AGE_RANGE_CHOICES = [
    ('<18', _('<18')),
    ('18-30', _('18-30')),
    ('31-45', _('31-45')),
    ('46-60', _('46-60')),
    ('>60', _('over 60')),
]

PLATFORM_CHOICES = [
    ('tw', _('Twitter')),
    ('fb', _('Facebook')),
    ('web', _('Website')),
    ('wa', _('WhatsApp')),
    ('yt', _('Youtube')),
    ('ig', _('Instagram')),
    ('other', _('Other')),
]

STATUS_CHOICES = [
    ('open', _('Open')),
    ('closed', _('Closed')),
    ('abstenia', _('In abstentia subject to appeal or objection')),
    ('na', _('Not applicable')),
]

class Defendant(models.Model):
    first_name = models.CharField(max_length=40, verbose_name=_('first name'))
    last_name = models.CharField(max_length=40, verbose_name=_('last name'))
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name=_('gender'))
    age_range = models.CharField(max_length=6, choices=AGE_RANGE_CHOICES, verbose_name=_('age range'))
    citizenship = models.CharField(max_length=6, choices=CITIZENSHIP_CHOICES, verbose_name=_('citizenship'))
    profession = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('profession'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Plaintiff(models.Model):
    first_name = models.CharField(max_length=40, verbose_name=_('first name'))
    last_name = models.CharField(max_length=40, verbose_name=_('last name'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class LawArticle(models.Model):
    number = models.CharField(max_length=100, verbose_name=_('number'))
    name = models.CharField(max_length=100, verbose_name=_('name'))

    def __str__(self):
        return self.number

class Case(Displayable):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('name'))
    summary = models.TextField(blank=True, verbose_name=_('summary'))
    defendants = models.ManyToManyField(Defendant, blank=True, verbose_name=_('defendants'))
    plaintiffs = models.ManyToManyField(Plaintiff, blank=True, verbose_name=_('plaintiffs'))
    date = models.DateTimeField(blank=True, null=True, verbose_name=_('date'))
    platform = models.CharField(max_length=6, blank=True, null=True, choices=PLATFORM_CHOICES, verbose_name=_('platform'))
    current_status = models.CharField(max_length=6, blank=True, null=True, choices=STATUS_CHOICES, verbose_name=_('status'))

    # expression details 
    charge = models.TextField(blank=True, null=True, verbose_name=_('charge'))
    charged_using = models.ManyToManyField(LawArticle, verbose_name=_('charged using law article') )
    bail = models.CharField(max_length=15, blank=True, null=True, verbose_name=_('bail amount'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.id 