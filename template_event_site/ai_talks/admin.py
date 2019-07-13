from django.contrib import admin

# Register your models here.
from ai_talks.models import Speaker, Staff, StaticParts, ScientificCommittee

admin.site.register(Speaker)
admin.site.register(Staff)
admin.site.register(StaticParts)
admin.site.register(ScientificCommittee)
