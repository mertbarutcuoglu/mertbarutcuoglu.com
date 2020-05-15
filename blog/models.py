from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Ready to publish")
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    @property
    def estimated_reading_time(self):
       word_count = len(self.content.split())
       reading_time = round(word_count/250)
       return reading_time
 
    def __str__(self):
        return self.title