from django.db import models

class About(models.Model):
    about_heading = models.CharField(max_length=20)
    about_discription = models.TextField(max_length=290)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading