from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError







class Post(models.Model):
   author = models.ForeignKey(
      User, 
      on_delete=models.CASCADE,
      verbose_name='Преподаватель'
   )
   title = models.CharField(
      max_length=100,
      verbose_name='Название'
   )
   text = models.TextField(
      verbose_name='Вопрос'
   )
   img = models.ImageField(upload_to='posts_images', blank=True)
   date = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return self.title
   
   def get_absolute_url(self):
      return reverse('news_detail_url', kwargs={'pk':self.pk})

   def get_comment_count(self):
      return self.comments.all().filter(approved=True).count()

   def clean(self):
      if self.author.profile.student == True:
         raise ValidationError('Пользователь не преподаватель')

   def save(self, *args, **kwargs):
      self.full_clean()
      return super().save(*args, **kwargs)

   class Meta:
      verbose_name = 'Тест'
      verbose_name = 'Тесты'


class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments' )
   full_name = models.CharField(max_length=50)
   img = models.ImageField(default='default.jpg', upload_to='user_images')
   text = models.TextField()
   date = models.DateTimeField(default=timezone.now)
   approved = models.BooleanField(default=True)

   def __str__(self):
      return 'Комментарий для поста "{}". {}'.format(self.post, self.text)

   
  