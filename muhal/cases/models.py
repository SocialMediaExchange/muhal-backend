from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

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
    ('jordan', _('Jordanian')),
    ('syria', _('Syrian')),
    ('palestine', _('Palestine')),
    ('stateless', _('Stateless')),
    ('unknown', _('Unknown')),
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
    ('pending', _('Pending appeal or objection')),
    ('unknown', _('Unknown')),
    # ('na', _('Not applicable')),
    # TODO verify if NA is an option for status
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
    ('publications', _('Publications court')),
    ('cassation', _('Cassation court')),
    ('appeals', _('Appellant court')),
    ('criminal', _('Criminal court')),
    ('military police', _('Military police centre')),
    ('army intel', _('Army Intelligence Branch')),
    ('military court', _('Military court')),
    ('state security', _('State security apparatus')),
    ('justice palace', _('Palace of Justice')),
    ('criminal investigations', _('Central bureau of criminal investigations')),
    ('public prosecutor', _('Executive public prosecutor')),
    ('general security', _('General security')),
]

KAZA_CHOICES = [
    (_('Lebanon'), (
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
    )),
    (_('Jordan'), (
        ('Irbid', _('Irbid')),
        ('Ajloun', _('Ajloun')),
        ('Jerash', _('Jerash')),
        ('Mafraq', _('Mafraq')),
        ('Balqa', _('Balqa')),
        ('Amman', _('Amman')),
        ('Zarqa', _('Zarqa')),
        ('Madaba', _('Madaba')),
        ('Karak', _('Karak')),
        ('Tafilah', _('Tafilah')),
        ('Ma’an', _('Ma’an')),
        ('Aqaba', _('Aqaba')),
    ))
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
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('description'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('defendant')
        verbose_name_plural = _('defendants')


class Plaintiff(models.Model):
    first_name = models.CharField(max_length=40, blank=True, null=True, verbose_name=_('first name'))
    last_name = models.CharField(max_length=40, blank=True, null=True, verbose_name=_('last name'))
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('description'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('plaintiff')
        verbose_name_plural = _('plaintiffs')


class Judge(models.Model):
    first_name = models.CharField(max_length=40, verbose_name=_('first name'))
    last_name = models.CharField(max_length=40, verbose_name=_('last name'))
    legal_entity = models.CharField(max_length=25, choices=LEGAL_ENTITY_CHOICES, verbose_name=_('legal entity'))
    kaza = models.CharField(max_length=20, choices=KAZA_CHOICES, blank=True, null=True, verbose_name=_('kaza'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('judge')
        verbose_name_plural = _('judge')


class LawArticle(models.Model):
    law = models.CharField(max_length=20, null=True, choices=LAW_CHOICES, verbose_name=_('law'))
    number = models.CharField(max_length=100, verbose_name=_('number'), help_text=_('Prefix the number with article or articles, to make sure it renders as a complete sentence'))
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('name'))
    url = models.URLField(blank=True, null=True, verbose_name=_('URL'), help_text=_('URL to the law text on the Lebanese University Centre for Law'))

    class Meta:
        verbose_name = _('law article')
        verbose_name_plural = _('law articles')

    def __str__(self):
        return '{} {}: {}'.format(self.get_law_display(), self.number, self.name)


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
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, verbose_name=_('country'))

    # basic info
    summary = models.TextField(blank=True, verbose_name=_('summary'))
    defendants = models.ManyToManyField(Defendant, blank=True, verbose_name=_('defendants'))
    plaintiffs = models.ManyToManyField(Plaintiff, blank=True, verbose_name=_('plaintiffs'))
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
    judges = models.ManyToManyField(Judge, blank=True, verbose_name=_('judges and their court'))
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

    # publishing 
    published = models.BooleanField(default=False, verbose_name=_('Published?'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    last_modified = models.DateTimeField(auto_now=True, verbose_name=_('Last modified'))

    def __str__(self):
        return self.summary[:15]

    # def clean(self):
    #     self.save()
    #     if self.published:
    #         errors = {}
    #         if not self.summary:
    #             errors['summary'] = _('The summary is missing')
    #             # raise ValidationError(_('The summary is missing'))
    #             # raise ValidationError({'summary': _('The summary is missing')})
    #         if not self.plaintiffs.all().exists():
    #             errors['plaintiffs'] = _('There needs to be at least one plaintiff')
    #             # raise ValidationError({'plaintiffs': _('There needs to be at least one plaintiff')})
    #         if not self.defendants.all().exists():
    #             errors['defendants'] = _('There needs to be at least one defendant')
    #             # raise ValidationError({'defendants': _('There needs to be at least one defendant')})
    #         if not self.current_status:
    #             errors['current_status'] = _('The current status is missing')
    #             # raise ValidationError({'current_status': _('The current status is missing')})
    #         if not self.platform:
    #             errors['platform'] = _('The platform is missing')
    #             # raise ValidationError({'platform': _('The platform is missing')})
    #         if not self.date_of_publication:
    #             errors['date_of_publication'] = _('The date of publication is missing')
    #             # raise ValidationError({'date_of_publication': _('The date of publication is missing')})
    #         if errors:
    #             self.published = False
    #             self.save()
    #             raise ValidationError(errors)
 
    def get_absolute_url(self):
        return self.id 

    def plaintiffs_list(self):
        return _(', ').join([str(plaintiff) for plaintiff in self.plaintiffs.all()])

    def defendants_list(self):
        return _(', ').join([str(defendant) for defendant in self.defendants.all()])

    class Meta:
        verbose_name = _('case')
        verbose_name_plural = _('cases')



# import csv
# reader = csv.reader(open('/Users/majdal/Downloads/People-Grid view.csv'))

# for row in reader: 
#     print(row)
#     citizenship = row[9]
#     country_of_citizenship = None
#     if citizenship == 'Lebanese':
#         country_of_citizenship = 'lebanon'
#     elif citizenship == 'Syrian':
#         country_of_citizenship = 'syria'
#     elif citizenship == 'Palestinian':
#         country_of_citizenship = 'palestine'
#     else:
#         country_of_citizenship = 'unknown'        

#     _, created = Defendant.objects.get_or_create(first_name_en=row[2],
#                            first_name_ar=row[3],
#                            last_name_en=row[4],
#                            last_name_ar=row[5],
#                            gender=row[6].lower(),
#                            citizenship=country_of_citizenship,
#                            profession_en=row[11],
#                            profession_ar=row[12],
#                            age_range=row[14]
#                            )


# import csv
# reader = csv.reader(open('/Users/majdal/Downloads/Cases-English.csv'))

# for row in reader: 
#     defendant = row[1].split(',')
#     last_names = [r.split()[-1] for r in defendant]
#     ids = []
#     for name in last_names: 
#         defen = Defendant.objects.filter(last_name_en__contains=name)
#         if defen.exists():
#             ids.append(defen[0].id)
#     defendants = Defendant.objects.filter(id__in=ids)

#     platform = row[5].lower()
#     if platform == 'twitter':
#         pltfrm = 'tw'
#     elif platform == 'facebook':
#         pltfrm = 'fb'
#     elif platform == 'instagram':
#         pltfrm = 'ig'
#     elif platform == 'website':
#         pltfrm = 'web'
#     elif platform == 'youtube':
#         pltfrm = 'yt'
#     elif platform == 'whatsapp':
#         pltfrm = 'wa'
#     else:
#         pltfrm = 'other'

#     status = row[7].lower()
#     if status == 'open':
#         stts = 'open'
#     elif status == 'closed':
#         stts = 'closed'
#     else:
#         stts = 'unknown'

#     c, created = Case.objects.get_or_create(
#             country = 'lebanon',

#     summary = row[6],
#     # defendants = defendants,
#     # plaintiffs = data is too dirty, cannot automatically import
#     platform = pltfrm,
#     current_status = stts
#                            )
#     print(created)
#     c.defendants.set(defendants)
#     c.save()













# ['Primary',
#  'Year',
#  'Court/police station information',
#  'Complaint by',
#  'Complaint',
#  'Source',
#  'Complaint_ar',
#  'Field 27']