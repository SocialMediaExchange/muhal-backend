from django.db import models
from django.utils.translation import gettext_lazy as _

COUNTRY_CHOICES = [
    ('lebanon', _('Lebanon')),
    ('jordan', _('Jordan')),
    ('other', _('Other')),
]

GENDER_CHOICES = [
    ('male', _('Male')),
    ('female', _('Female')),
    ('other', _('Other')),
]

CITIZENSHIP_CHOICES = [
    ('lebanon', _('Lebanese')),
    ('syria', _('Syrian')),
    ('stateless', _('Stateless')),
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
    ('refuse', _('Refused signing')),
    ('n/a', _('Not applicable')),
]

DELETE_CONTENT_CHOICES = [
    ('forced', _('Forced to delete')),
    ('required', _('Required to delete')),
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

LAW_CHOICES = [
    ('publication', _('Publications law')),
    ('penal', _('Penal code')),
    ('electronic', _('Electronic affairs')),
    ('military', _('Military law')),
    ('other', _('Other')),
]

class Defendant(models.Model):
    first_name = models.CharField(max_length=40, verbose_name=_('first name'))
    last_name = models.CharField(max_length=40, verbose_name=_('last name'))
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name=_('gender'))
    age_range = models.CharField(max_length=6, choices=AGE_RANGE_CHOICES, verbose_name=_('age range'))
    citizenship = models.CharField(max_length=10, choices=CITIZENSHIP_CHOICES, verbose_name=_('citizenship'))
    profession = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('profession'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('defendant')
        verbose_name_plural = _('defendants')


class Plaintiff(models.Model):
    first_name = models.CharField(max_length=40, verbose_name=_('first name'))
    last_name = models.CharField(max_length=40, verbose_name=_('last name'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('plaintiff')
        verbose_name_plural = _('plaintiffs')


class Judge(models.Model):
    first_name = models.CharField(max_length=40, verbose_name=_('first name'))
    last_name = models.CharField(max_length=40, verbose_name=_('last name'))
    legal_entity = models.CharField(max_length=10, choices=LEGAL_ENTITY_CHOICES, verbose_name=_('legal entity'))
    kaza = models.CharField(max_length=20, choices=KAZA_CHOICES, blank=True, null=True, verbose_name=_('kaza'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('judge')
        verbose_name_plural = _('judge')


class LawArticle(models.Model):
    law = models.CharField(max_length=20, null=True, choices=LAW_CHOICES, verbose_name=_('law'))
    number = models.CharField(max_length=100, verbose_name=_('number'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    url = models.URLField(blank=True, null=True, verbose_name=_('URL'), help_text=_('URL to the law text on the Lebanese University Centre for Law'))

    class Meta:
        verbose_name = _('law article')
        verbose_name_plural = _('law articles')

    def __str__(self):
        return _('{} article {}').format(self.law, self.number)


class Reference(models.Model):
    case = models.ForeignKey('Case', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name=_('title'))
    url = models.URLField(verbose_name=_('URL'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Reference')
        verbose_name_plural = _('References')


class Case(models.Model):
    # country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, verbose_name=_('country'))

    # basic info
    summary = models.TextField(blank=True, verbose_name=_('summary'))
    defendants = models.ManyToManyField(Defendant, blank=True, verbose_name=_('defendants'))
    plaintiffs = models.ManyToManyField(Plaintiff, blank=True, verbose_name=_('plaintiffs'))
    # date = models.DateField(blank=True, null=True, verbose_name=_('publication date'))
    platform = models.CharField(max_length=6, blank=True, null=True, choices=PLATFORM_CHOICES, verbose_name=_('platform'))
    current_status = models.CharField(max_length=8, blank=True, null=True, choices=STATUS_CHOICES, verbose_name=_('status'))

    # complaint details
    station_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('Police station name'))
    detained = models.CharField(max_length=6, blank=True, null=True, choices=YES_NO_NA_CHOICES, verbose_name=_('detained?'))
    detained_for = models.IntegerField(blank=True, null=True, verbose_name=_('detained for number of days'))
    pledge_signing = models.CharField(max_length=6, blank=True, null=True, choices=PLEDGE_SIGNING_CHOICES, verbose_name=_('Requested to sign pledge?'))
    content_deletion = models.CharField(max_length=10, blank=True, null=True, choices=DELETE_CONTENT_CHOICES, verbose_name=_('Requested to delete content?'))
    reconciliation = models.NullBooleanField(verbose_name=_('reconciliation'))

    # Case details
    # expression details 
    charge = models.TextField(blank=True, null=True, verbose_name=_('charge'))
    charged_using = models.ManyToManyField(LawArticle, blank=True, verbose_name=_('charged using law article') )
    bail = models.IntegerField(blank=True, null=True, verbose_name=_('bail amount'), help_text=_('The amount in local currency'))

    # interrogation and detention 
    sentenced = models.CharField(max_length=9, blank=True, null=True, choices=SENTENCED_CHOICES, verbose_name=_('sentenced?'))
    sentence = models.TextField(blank=True, null=True, verbose_name=_('sentence'))
    in_absentia = models.CharField(max_length=6, blank=True, null=True, choices=YES_NO_NA_CHOICES, verbose_name=_('in absentia?'))
    content_deletion = models.CharField(max_length=10, blank=True, null=True, choices=DELETE_CONTENT_CHOICES, verbose_name=_('Requested to delete content?'))
    contacted_via = models.CharField(max_length=10, blank=True, null=True, choices=CONTACTED_VIA_CHOICES, verbose_name=_('Contacted via'))

    # interrogation and detention 
    judge = models.ForeignKey(Judge, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_('judge and court'))
    # sentenced = models.CharField(max_length=6, blank=True, null=True, choices=SENTENCED_CHOICES, verbose_name=_('sentenced?'))
    sentence = models.TextField(blank=True, null=True, verbose_name=_('sentence'))
    in_absentia = models.CharField(max_length=6, blank=True, null=True, choices=YES_NO_NA_CHOICES, verbose_name=_('in absentia?'))
    contacted_via = models.CharField(max_length=10, blank=True, null=True, choices=CONTACTED_VIA_CHOICES, verbose_name=_('Contacted via'))

    # timeline
    date_of_publication = models.DateField(blank=True, null=True, verbose_name=_('date of publication'))
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

    def plaintiffs_list(self):
        return _(', ').join([str(plaintiff) for plaintiff in self.plaintiffs.all()])

    def defendants_list(self):
        return _(', ').join([str(defendant) for defendant in self.defendants.all()])

    class Meta:
        verbose_name = _('case')
        verbose_name_plural = _('cases')