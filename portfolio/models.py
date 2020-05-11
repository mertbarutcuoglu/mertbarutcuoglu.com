from django.db import models

class Technology(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    is_on_github = models.BooleanField()
    github_link = models.URLField(blank=True, null=True)
    is_on_blog = models.BooleanField()
    blog_link = models.URLField(blank=True, null=True)
    used_technologies = models.ManyToManyField(Technology)

    def __str__(self):
        return self.title

