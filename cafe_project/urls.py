# urls.py

from django.urls import path
#from . import views
from cafe_app import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cafe_app.views import *
from cafe_app.views import gallery
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('specials/', specials, name='specials'),
    path('reviews/', reviews, name='reviews'),
    path('add_review/', add_review, name='add_review'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)