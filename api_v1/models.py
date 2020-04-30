from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='<title>')
    description = models.CharField(max_length=200,
                                   blank=False,
                                   default='<desc>')
    published = models.BooleanField(default=False)
