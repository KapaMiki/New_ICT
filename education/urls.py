from django.urls import path
from .views import group_students


urlpatterns = [
    path('group-students/', group_students, name='group_students_url')
]

