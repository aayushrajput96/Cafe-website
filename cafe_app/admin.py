from django.contrib import admin
from .models import Special
from .models import MenuItem
from .models import GalleryImage

admin.site.register(Special)
admin.site.register(MenuItem)
admin.site.register(GalleryImage)