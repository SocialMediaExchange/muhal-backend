from django.db import models
from mezzanine.core.models import Displayable
from django.utils.translation import gettext_lazy as _

COUNTRY_CHOICES = [
    ('lb', _('Lebanon')),
    ('jo', _('Jordan')),
    ('other', _('Other')),
]

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

SENTENCED_CHOICES = [
    ('yes', _('Yes')),
    ('no', _('No')),
    ('postponed', _('Postponed')),
    ('inprocess', _('In the process')),
    ('n/a', _('Not applicable')),
]

YES_NO_NA_CHOICES = [
    ('yes', _('Yes')),
    ('no', _('No')),
    ('n/a', _('Not applicable')),
]

PLEDGE_SIGNING_CHOICES = [
    ('yes', _('Yes')),
    ('no', _('No')),
    ('refuse', _('Refused')),
    ('n/a', _('Not applicable')),
]

DELETE_CONTENT_CHOICES = [
    ('forced', _('Forced')),
    ('required', _('Required')),
    ('No', _('No')),
    ('n/a', _('Not applicable')),
]

CONTACTED_VIA_CHOICES = [
    ('phone', _('Phone call')),
    ('inperson', _('In person')),
    ('fax', _('Fax')),
    ('No', _('No')),
]

LEGAL_ENTITY_CHOICES = [
    ('army intel', _('Army Intelligence Branch')),
]

KAZA_CHOICES = [
    ('Akkar', _('Akkar')),
    ('Minieh-Danieh', _('Minieh-Danieh')),
    ('Baalbeck', _('Baalbeck')),
    ('Hermel', _('Hermel')),
    ('Beirut', _('Beirut')),
    ('Rachiaya', _('Rachiaya')),
    ('West Bekaa', _('West Bekaa')),
    ('Zahleh', _('Zahleh')),
    ('Aley', _('Aley')),
    ('Baabda', _('Baabda')),
    ('Batroun', _('Batroun')),
    ('Chouf', _('Chouf')),
    ('El Metn', _('El Metn')),
    ('Jezzine', _('Jezzine')),
    ('Jubail', _('Jubail')),
    ('Kasrouane', _('Kasrouane')),
    ('Bint Jbayl', _('Bint Jbayl')),
    ('Hasbaya', _('Hasbaya')),
    ('Marjaayoun', _('Marjaayoun')),
    ('Nabatiyeh', _('Nabatiyeh')),
    ('Batroun', _('Batroun')),
    ('Bcharre', _('Bcharre')),
    ('Koura', _('Koura')),
    ('Minieh-Danieh', _('Minieh-Danieh')),
    ('Tripoli', _('Tripoli')),
    ('Zgharta', _('Zgharta')),
    ('Jezzine', _('Jezzine')),
    ('Nabatiyeh', _('Nabatiyeh')),
    ('Saida', _('Saida')),
    ('Sour', _('Sour')),
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

class Judge(models.Model):
    first_name = models.CharField(max_length=40, verbose_name=_('first name'))
    last_name = models.CharField(max_length=40, verbose_name=_('last name'))
    legal_entity = models.CharField(max_length=6, choices=LEGAL_ENTITY_CHOICES, verbose_name=_('legal entity'))
    kaza = models.CharField(max_length=20, choices=KAZA_CHOICES, blank=True, null=True, verbose_name=_('kaza'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class LawArticle(models.Model):
    number = models.CharField(max_length=100, verbose_name=_('number'))
    name = models.CharField(max_length=100, verbose_name=_('name'))

    def __str__(self):
        return self.number

class Case(Displayable):
    country = models.CharField(max_length=5, choices=COUNTRY_CHOICES, verbose_name=_('country'))

    # basic info
    # name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('web title'))
    summary = models.TextField(blank=True, verbose_name=_('summary'))
    defendants = models.ManyToManyField(Defendant, blank=True, verbose_name=_('defendants'))
    plaintiffs = models.ManyToManyField(Plaintiff, blank=True, verbose_name=_('plaintiffs'))
    date = models.DateTimeField(blank=True, null=True, verbose_name=_('date'))
    platform = models.CharField(max_length=6, blank=True, null=True, choices=PLATFORM_CHOICES, verbose_name=_('platform'))
    current_status = models.CharField(max_length=6, blank=True, null=True, choices=STATUS_CHOICES, verbose_name=_('status'))

    # expression details 
    charge = models.TextField(blank=True, null=True, verbose_name=_('charge'))
    charged_using = models.ManyToManyField(LawArticle, blank=True, verbose_name=_('charged using law article') )
    bail = models.CharField(max_length=15, blank=True, null=True, verbose_name=_('bail amount'))

    # interrogation and detention 
    sentenced = models.CharField(max_length=6, blank=True, null=True, choices=SENTENCED_CHOICES, verbose_name=_('sentenced?'))
    sentence = models.TextField(blank=True, null=True, verbose_name=_('sentence'))
    in_absentia = models.CharField(max_length=6, blank=True, null=True, choices=YES_NO_NA_CHOICES, verbose_name=_('in absentia?'))
    detained = models.CharField(max_length=6, blank=True, null=True, choices=YES_NO_NA_CHOICES, verbose_name=_('detained?'))
    detained_for = models.IntegerField(blank=True, null=True, verbose_name=_('detained for number of days'))
    pledge_signing = models.CharField(max_length=6, blank=True, null=True, choices=PLEDGE_SIGNING_CHOICES, verbose_name=_('Requested to sign pledge?'))
    content_deletion = models.CharField(max_length=10, blank=True, null=True, choices=DELETE_CONTENT_CHOICES, verbose_name=_('Requested to delete content?'))
    contacted_via = models.CharField(max_length=10, blank=True, null=True, choices=CONTACTED_VIA_CHOICES, verbose_name=_('Contacted via'))

    # interrogation and detention 
    judge = models.ForeignKey(Judge, blank=True, null=True, verbose_name=_('judge and court'))
    sentenced = models.CharField(max_length=6, blank=True, null=True, choices=SENTENCED_CHOICES, verbose_name=_('sentenced?'))
    sentence = models.TextField(blank=True, null=True, verbose_name=_('sentence'))
    in_absentia = models.CharField(max_length=6, blank=True, null=True, choices=YES_NO_NA_CHOICES, verbose_name=_('in absentia?'))
    detained = models.CharField(max_length=6, blank=True, null=True, choices=YES_NO_NA_CHOICES, verbose_name=_('detained?'))
    detained_for = models.IntegerField(blank=True, null=True, verbose_name=_('detained for number of days'))
    pledge_signing = models.CharField(max_length=6, blank=True, null=True, choices=PLEDGE_SIGNING_CHOICES, verbose_name=_('Requested to sign pledge?'))
    content_deletion = models.CharField(max_length=10, blank=True, null=True, choices=DELETE_CONTENT_CHOICES, verbose_name=_('Requested to delete content?'))
    contacted_via = models.CharField(max_length=10, blank=True, null=True, choices=CONTACTED_VIA_CHOICES, verbose_name=_('Contacted via'))

    # timeline
    date_of_post = models.DateField(blank=True, null=True, verbose_name=_('date of publication of expression'))
    date_of_contact = models.DateField(blank=True, null=True, verbose_name=_('date of contact by cybercrime bureau'))
    date_of_investigation = models.DateField(blank=True, null=True, verbose_name=_('date of investigation'))
    date_of_detention = models.DateField(blank=True, null=True, verbose_name=_('date of detention'))
    duration_of_detention = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_('duration of detention (in days)'))
    date_of_hearing = models.DateField(blank=True, null=True, verbose_name=_('date of hearing'))
    date_of_hearing_2 = models.DateField(blank=True, null=True, verbose_name=_('date of second hearing'))
    date_of_release = models.DateField(blank=True, null=True, verbose_name=_('date of release'))
    date_of_ruling = models.DateField(blank=True, null=True, verbose_name=_('date of ruling'))


    def __str__(self):
        return self.summary[:15]

    def get_absolute_url(self):
        return self.id 