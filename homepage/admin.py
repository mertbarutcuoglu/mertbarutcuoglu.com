from django.contrib import admin
from .views import Bio, Section
from django_summernote.admin import SummernoteModelAdmin

class BioAdmin(SummernoteModelAdmin):
    summernote_fields = ('summary',)


admin.site.register(Bio, BioAdmin)
admin.site.register(Section)