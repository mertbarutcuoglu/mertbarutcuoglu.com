import sys
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
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
    image = models.ImageField()
    section_emoji = models.IntegerField() # dec value for emoji
    links_to = models.URLField()

    def save(self):
        im = Image.open(self.image)

        output = BytesIO()

        im = im.resize((290, 352))

        im.save(output, format='JPEG', quality=95)
        output.seek(0)

        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Section, self).save()

    def __str__(self):
        return self.title