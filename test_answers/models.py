from django.db import models
from News.models import Post
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class Answer(models.Model):
    test = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Тест'
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    answer = models.TextField(
        verbose_name='Ответ'
    )
    data = models.FileField(
        verbose_name='Файл',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    
    def __str__(self):
        return f'Ответ студента {self.student.first_name} {self.student.last_name} на тест: {self.test.title}'

    def clean(self):
        if self.student.profile.student != True:
            raise ValidationError('Этот пользователь не студент')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)