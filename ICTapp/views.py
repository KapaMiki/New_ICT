from django.shortcuts import render, get_object_or_404
from .models import Information
from django.views.generic import View
from .models import Specialty
from django.contrib.auth.models import User
from News.models import Post
from Users.models import Profile
import os
from django.conf import settings
from django.http import HttpResponse, Http404

def home(request):
   posts = Post.objects.filter().order_by('-date')[:4]
   return render(request, 'ICTapp/index.html', context={
      'posts': posts,
   })


def informations(request):
   informations = Information.objects.all()
   return render(request, 'ICTapp/informations.html', context={'informations': informations})

class InformationDetailView(View):
   def get(self, request, pk):
      information = get_object_or_404(Information, pk=pk)
      latest_news = Post.objects.filter().order_by('-date')[:3]
      return render(request, 'ICTapp/information_detail.html', context={
         'information': information,
         'latest_news': latest_news,
      })


class SpecialtyView(View):
   def get(self, request):
      specialty = Specialty.objects.all()
      return render(request, 'ICTapp/specialty.html', context={
         'specialty': specialty,
      })


class SpecialtyDetailView(View):
   def get(self, request, slug):
      speciality = get_object_or_404(Specialty, slug=slug)
      latest_news = Post.objects.filter().order_by('-date')[:3]
      return render(request, 'ICTapp/specialty_detail.html', context={
         'speciality': speciality,
         'latest_news': latest_news,
      })


class StaffView(View):
   def get(self, request):
      user_1 = User.objects.get(id=1)
      dekan = User.objects.get(username='shaikhanova')
      zam_dekana = User.objects.get(username='adylkanova')
      zaf_kafedry = User.objects.get(username='zolotov')
      ospanov = User.objects.get(username='ospanov')
      sekerbaeva = User.objects.get(username='sekerbaeva')
      myassoedov = User.objects.get(username='myassoedov')
      kurushbaeva = User.objects.get(username='kurushbaeva')
      nazarov = User.objects.get(username='nazarov')
      return render(request, 'ICTapp/staff.html', context={
         'user_1': user_1,
         'dekan': dekan,
         'zam_dekana': zam_dekana,
         'zaf_kafedry': zaf_kafedry,
         'ospanov': ospanov,
         'sekerbaeva': sekerbaeva,
         'myassoedov': myassoedov,
         'kurushbaeva': kurushbaeva,
         'nazarov': nazarov,
      })


class StaffDetailView(View):
   def get(self, request, pk):
      user = get_object_or_404(Profile, pk=pk)
      return render(request, 'ICTapp/staff_detail.html', context={'user': user})


def download_lecture(request, id):
   file = get_object_or_404(Specialty, id=id)
   file_path = file.data.path
   if os.path.exists(file_path):
      with open(file_path, 'rb') as fh:
         response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
         return response
   raise Http404


def download_practice(request, id):
   file = get_object_or_404(Information, id=id)
   file_path = file.data.path
   if os.path.exists(file_path):
      with open(file_path, 'rb') as fh:
         response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
         return response
   raise Http404