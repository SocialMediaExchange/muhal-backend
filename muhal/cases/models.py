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

class Accused(models.Model):
    first_name = models.CharField(max_length=40, verbose_name=_('first name'))
    last_name = models.CharField(max_length=40, verbose_name=_('last name'))
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name=_('gender'))
    age_range = models.CharField(max_length=6, choices=AGE_RANGE_CHOICES, verbose_name=_('age range'))
    citizenship = models.CharField(max_length=6, choices=CITIZENSHIP_CHOICES, verbose_name=_('citizenship'))
    profession = models.CharField(max_length=100, verbose_name=_('profession'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Case(Displayable):
    name = models.CharField(max_length=100, verbose_name=_('name'))