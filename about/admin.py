from django.contrib import admin
from .models import About

# Register your models here.

class aboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False

admin.site.register(About, aboutAdmin)