from django.urls import path
from .views import (
   home, 
   informations, 
   InformationDetailView, 
   SpecialtyView, 
   SpecialtyDetailView, 
   StaffView, 
   StaffDetailView, 
   download_lecture,
   download_practice
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', home, name='home_url'),
   path('practices/', informations, name='informations_url'),
   path('practices/download/<int:id>/', download_practice, name='download_practice'),
   # path('student-life/<int:pk>/', InformationDetailView.as_view(), name='information_detail_url'),
   path('lectures/', SpecialtyView.as_view(), name='specialty_url'),
   # path('specialty/<str:slug>/', SpecialtyDetailView.as_view(), name='specialty_detail_url'),
   path('staff/', StaffView.as_view(), name='staff_url'),
   path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail_url'),
   path('lectures/download/<int:id>/', download_lecture, name='download_lecture')
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)