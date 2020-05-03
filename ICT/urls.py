from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ICTapp.urls')),
    path('tests/', include('News.urls')),
    path('account/', include('Users.urls')),
    path('semester/', include('semesters.urls')),
    path('education/', include('education.urls'))
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)