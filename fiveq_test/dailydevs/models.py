# Django imports
from django.db import models
# Third-party imports
from taggit.managers import TaggableManager


class Devotion(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    body = models.TextField(null=True)
    tags = TaggableManager()

    def __unicode__(self):
        return '%s: %s' % (self.date, self.title)
