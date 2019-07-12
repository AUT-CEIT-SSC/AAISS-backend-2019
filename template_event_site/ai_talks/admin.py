from django.contrib import admin

# Register your models here.
from ai_talks.models import Speaker, Staff

admin.site.register(Speaker)
admin.site.register(Staff)

