from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from movie import views as movieViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movieViews.index),
    path('signup/', movieViews.signup, name='signup'),
    path('about/', movieViews.about, name='about'),
    path('contact/', movieViews.contact, name='contact'),
    path('schedule/', movieViews.schedule, name='schedule'),
    path('classes/', movieViews.classes, name='classes'),


    
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
