from django.db import models
from django.utils import timezone
from django.urls import reverse



class Information(models.Model):
   title = models.CharField(max_length=100, verbose_name='Название')
   text = models.TextField(verbose_name='Описание')
   img_main = models.ImageField(upload_to='practice_images', blank=False, verbose_name='Главная фотография')
   data = models.FileField(upload_to='practices/', verbose_name='Файл')
   date = models.DateTimeField(default=timezone.now)

   class Meta:
      verbose_name = 'Практическое задание'
      verbose_name_plural = 'Практические задания'

   def __str__(self):
      return self.title
   
   # def get_absolute_url(self):
   #    return reverse('information_detail_url', kwargs={'pk':self.pk})


class Specialty(models.Model):
   name = models.CharField(max_length=100, verbose_name='Название')
   img = models.ImageField(upload_to='Specialty_images', verbose_name='Фотография')
   data = models.FileField(upload_to='lectures/', verbose_name='Файл')

   def __str__(self):
      return self.name

   class Meta:
      verbose_name = 'Лекция'
      verbose_name_plural = 'Лекции'
   
   # def get_absolute_url(self):
   #    return reverse('specialty_detail_url', kwargs={'slug':self.slug})


class Discipline(models.Model):
   specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="disciplines")
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name



class Question(models.Model):
   full_name = models.CharField(max_length=50)
   email = models.EmailField()
   phone = models.IntegerField()
   text = models.TextField()

   def __str__(self):
      return self.text