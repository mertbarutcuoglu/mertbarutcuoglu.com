from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Ready to publish")
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return self.title