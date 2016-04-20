from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import locale


locale.setlocale(locale.LC_ALL, '')


class ProjectProposal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    challenge = models.CharField(max_length=1023, null=False, blank=False)
    proposal = models.CharField(max_length=1023, null=False, blank=False)
    organization = models.CharField(max_length=255, null=False, blank=False)

    output = models.CharField(max_length=255)
    output_indicators = models.CharField(max_length=255)

    outcomes = models.CharField(max_length=255)
    outcomes_indicators = models.CharField(max_length=255)

    impact = models.CharField(max_length=255)
    impact_indicators = models.CharField(max_length=255)

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    multiplier = models.FloatField(null=False, blank=False, default=1.0)
    initial_multiplier = models.FloatField(null=False, blank=False, default=1.0)

    supporting_users = models.ManyToManyField(User, blank=True, related_name='projects_supported')
    logo = models.ImageField(upload_to='static/media')
    picture = models.ImageField(upload_to='static/media')
    link = models.URLField()

    # TODO: implement repr

    def __str__(self):
        return 'Project proposal by {org}'.format(org=self.organization)

    def str_amount(self):
        return locale.currency(self.amount, grouping=True)

    def logo_url(self):
        return 'media/{url}'.format(url=self.logo.url)

    def picture_url(self):
        return 'media/{url}'.format(url=self.picture.url)


class UserProjectSupportLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, null=False, related_name='projects_supported_log')
    project = models.ForeignKey(ProjectProposal, null=False, related_name='supporting_users_log')

    current_multiplier = models.FloatField(null=False, blank=False)


USER_ACTION = 'User action'
AUTOMATIC = 'Automatic'
MANUAL = 'Manual'
MULTIPLIER_CHANGE_CAUSES = (
    (USER_ACTION, USER_ACTION),
    (AUTOMATIC, AUTOMATIC),
    (MANUAL, MANUAL)
)


class MultiplierChangeLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    previous_multiplier = models.FloatField(null=False, blank=False)
    current_multiplier = models.FloatField(null=False, blank=False)

    cause = models.CharField(max_length=255, choices=MULTIPLIER_CHANGE_CAUSES)
    related_log = models.OneToOneField(UserProjectSupportLog, null=True)
