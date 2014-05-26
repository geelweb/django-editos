from django.db import models
from geelweb.django.editos import settings

class Edito(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    button_label = models.CharField(max_length=20, default="Go !",
            Required=False)
    image = models.FileField(upload_to="editos")
    text_content = models.CharField(max_length=400)
    display_from = models.DateField()
    display_until = models.DateField()
    active = models.BooleanField(default=True)
    text_theme = models.CharField(max_length=10, choices=settings.EDITOS_THEMES,
            default=settings.EDITOS_DEFAULT_THEME)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
