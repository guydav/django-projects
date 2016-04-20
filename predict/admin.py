from django.contrib import admin

import models


class ProjectProposalAdmin(admin.ModelAdmin):
    list_display = (
        'organization',
        'challenge',
        'proposal',
        'str_amount',
        'multiplier'
    )

    list_display_links = (
        'organization',
        'challenge',
        'proposal',
    )

admin.site.register(models.ProjectProposal, ProjectProposalAdmin)
admin.site.register(models.UserProjectSupportLog)
admin.site.register(models.MultiplierChangeLog)