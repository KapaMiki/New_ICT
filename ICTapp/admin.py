from django.contrib import admin
from .models import Information, Specialty, Discipline, Question


admin.site.register(Information)
admin.site.register(Specialty)
admin.site.register(Discipline)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
   list_display = ['full_name', 'email', 'phone', 'text']
