from django.utils.translation import ugettext as _
from django.db import models

"""Contains details for fixed sets of choices for validation and data homogenaity"""

DAY_OF_THE_WEEK = {
    '1' : _(u'Monday'),
    '2' : _(u'Tuesday'),
    '3' : _(u'Wednesday'),
    '4' : _(u'Thursday'),
    '5' : _(u'Friday'),
    '6' : _(u'Saturday'), 
    '7' : _(u'Sunday'),
}

OCCURANCE_OPTIONS = {
    '1' : _(u'Daily'),
    '2' : _(u'Weekly'),
    '3' : _(u'Monthly'),
}

US_STATE = {
    'AL' : _(u'Alabama'),
    'AK' : _(u'Alaska'),
    'AZ' : _(u'Arizona'),
    'AR' : _(u'Arkansas'),
    'CA' : _(u'California'),
    'CO' : _(u'Colorado'),
    'CT' : _(u'Connecticut'),
    'DE' : _(u'Delaware'),
    'FL' : _(u'Florida'),
    'GA' : _(u'Georgia'),
    'HI' : _(u'Hawaii'),
    'ID' : _(u'Idaho'),
    'IL' : _(u'Illinois'),
    'IN' : _(u'Indiana'),
    'IA' : _(u'Iowa'),
    'KS' : _(u'Kansas'),
    'KY' : _(u'Kentucky'),
    'LA' : _(u'Louisiana'),
    'ME' : _(u'Maine'),
    'MD' : _(u'Maryland'),
    'MA' : _(u'Massachusetts'),
    'MI' : _(u'Michigan'),
    'MN' : _(u'Minnesota'),
    'MS' : _(u'Mississippi'),
    'MO' : _(u'Missouri'),
    'MT' : _(u'Montana'),
    'NE' : _(u'Nebraska'),
    'NV' : _(u'Nevada'),
    'NH' : _(u'New Hampshire'),
    'NJ' : _(u'New Jersey'),
    'NM' : _(u'New Mexico'),
    'NY' : _(u'New York'),
    'NC' : _(u'North Carolina'),
    'ND' : _(u'North Dakota'),
    'OH' : _(u'Ohio'),
    'OK' : _(u'Oklahoma'),
    'OR' : _(u'Oregon'),
    'PA' : _(u'Pennsylvania'),
    'RI' : _(u'Rhode Island'),
    'SC' : _(u'South Carolina'),
    'SD' : _(u'South Dakota'),
    'TN' : _(u'Tennessee'),
    'TX' : _(u'Texas'),
    'UT' : _(u'Utah'),
    'VT' : _(u'Vermont'),
    'VA' : _(u'Virginia'),
    'WA' : _(u'Washington'),
    'WV' : _(u'West Virginia'),
    'WI' : _(u'Wisconsin'),
    'WY' : _(u'Wyoming')
}

class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length']=1 
        super(DayOfTheWeekField,self).__init__(*args, **kwargs)

class OccuranceField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(OCCURANCE_OPTIONS.items()))
        kwargs['max_length']=1 
        super(OccuranceField,self).__init__(*args, **kwargs)

class USStateField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices']=tuple(sorted(US_STATE.items()))
        kwargs['max_length']=1 
        super(USStateField,self).__init__(*args, **kwargs)