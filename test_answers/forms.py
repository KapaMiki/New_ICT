from .models import Answer
from django import forms






class AnswerForm(forms.ModelForm):
   class Meta:
      model = Answer
      fields = ('student', 'answer', 'data')

#    def __init__(self, *args, **kwargs):
#       super(CommentForm, self).__init__(*args, **kwargs)
#       self.fields['full_name'].label = "Имя Фамилия"
#       self.fields['text'].label = "Текст"