from django.db import models
from django.utils.translation import ugettext_lazy as _


class Participant(models.Model):

    MAR = 'Mar'
    APR = 'Apr'
    MAY = 'May'

    MONTH_OPTIONS = ((MAR, _('March')),
                     (APR, _('April')),
                     (MAY, _('May')))

    surname = models.CharField(_('Surname'), max_length=255)
    first_name = models.CharField(_('First name'), max_length=255)
    school = models.CharField(_('School'), max_length=255)
    grade_level = models.CharField(_('Grade level'), max_length=255)
    city = models.CharField(_('City'), max_length=255)
    province = models.CharField(_('Province'), max_length=255)
    email = models.EmailField(_('Email address'), unique=True)
    preferred_course_start = models.CharField(_('Preferred course start'),
                                              max_length=3,
                                              choices=MONTH_OPTIONS)

    def __str__(self):
        return self.email
