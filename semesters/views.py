from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import (
   View,
   ListView,
   DetailView,
   CreateView,
   UpdateView,
   DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def semester(request):
   return render(request, 'semesters/index.html', context={
})


