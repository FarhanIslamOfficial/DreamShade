from django.contrib import admin

from gallery_app.models import (Album, Tag, Picture)


# Register your models here.
admin.site.register(Album)
admin.site.register(Tag)
admin.site.register(Picture)
