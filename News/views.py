from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages
from test_answers.forms import AnswerForm
from education.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
   View,
   ListView, 
   DetailView, 
   CreateView,
   UpdateView,
   DeleteView,
)




def news(request):
   posts = Post.objects.all()
   return render(request, 'News/news.html', context={
      'posts':posts,
   })


class ShowNewsView(ListView):
   model = Post
   template_name = 'News/news.html'
   context_object_name = 'posts'
   ordering = ['-date']
   paginate_by = 3

   def get_context_data(self, **kwargs):
      ctx = super(ShowNewsView, self).get_context_data(**kwargs)
      ctx['latest_news'] = Post.objects.filter().order_by('-date')[:3]
      return ctx 

class NewsDetailView(View):
   def get(self, request, pk):
      post = get_object_or_404(Post, pk=pk)
      latest_news = Post.objects.filter().order_by('-date')[:3]
      groups = Group.objects.all()
      answer_form = AnswerForm()
      return render(request, 'News/news_detail.html', context={
         'post': post,
         'answer_form': answer_form,
         'latest_news': latest_news,
         'groups':groups
      })

   def post(self, request, pk):
      post = get_object_or_404(Post, pk=pk)
      bound_form = CommentForm(request.POST)
      if bound_form.is_valid():
         text = request.POST.get('text')
         full_name = request.POST.get('full_name')
         comment = Comment.objects.create(post=post, full_name=full_name, text=text)
         comment.save()
         messages.success(request, f'Ваш комментарий в рассмотрений')
         return redirect(post)
      return redirect(post)


class CreateNewsView(LoginRequiredMixin, CreateView):
   model = Post
   fields = ('title', 'text', 'img', 'img_1', 'img_2', 'img_3', 'img_4')

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = Post
   template_name = 'News/post_update.html'
   fields = ('title', 'text', 'img', 'img_1', 'img_2', 'img_3', 'img_4')

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

   def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
         return True
      return False


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Post
   success_url = reverse_lazy('news_url')

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

   def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
         return True
      return False