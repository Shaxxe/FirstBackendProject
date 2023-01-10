from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include,path
from movie import views as movieViews
from accounts import views as accountsViews
from contact import views as contactViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movieViews.index, name='index'),
    path('signup/', movieViews.signup, name='signup'),
    path('about/', movieViews.about, name='about'),
    path('contact/', contactViews.contact, name='contact'),
    path('schedule/', movieViews.schedule, name='schedule'),
    path('classes/', movieViews.classes, name='classes'),
    path('accounts/', include('accounts.urls')),
    path('signupaccount/', accountsViews.signupaccount,name='signupaccount'),
    path('logout/', accountsViews.logoutaccount,name='logoutaccount'),
    path('login/', accountsViews.loginaccount,name='loginaccount'),
    path('program/<int:pk>/', movieViews.MyModelDetailView.as_view(),name='program_detail'),

    
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
