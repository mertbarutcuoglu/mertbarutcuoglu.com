from django.shortcuts import render
from .models import Bio, Section

def homepage_view(request, *args, **kwargs):
    personal_details = Bio.objects.get(id=1)
    sections = Section.objects.order_by('id')

    context = {
        'short_description': personal_details.short_description,
        'emoji': personal_details.short_description_emoji,
        'summary': personal_details.summary,
        'sections': sections
    }

    return render(request, "index.html", context)
