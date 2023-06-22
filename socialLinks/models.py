from django.db import models

class SocialLink(models.Model):
    platform = models.CharField(max_length=25, unique=True)
    platform_link = models.URLField(max_length=100)

    def __str__(self):
        return self.platform