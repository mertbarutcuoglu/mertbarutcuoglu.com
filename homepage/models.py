from django.db import models
from django.core.exceptions import ValidationError

class Bio(models.Model):
    summary = models.TextField()
    short_description = models.CharField(max_length=50)
    short_description_emoji = models.IntegerField() # dec value for emoji

    # make sures that there is only one instance of Bio 
    def save(self, *args, **kwargs):
        if not self.pk and Bio.objects.exists():
            raise ValidationError("Can't have more than one bio. Edit the existing one.")
        return super(Bio, self).save(*args, **kwargs)

class Section(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    #image = models.ImageField(upload_to='images')
    section_emoji = models.IntegerField() # dec value for emoji