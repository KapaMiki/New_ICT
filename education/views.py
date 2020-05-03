from django.shortcuts import render
from .models import Group
from django.shortcuts import get_object_or_404
from django.http import JsonResponse




def group_students(request):
    group = get_object_or_404(Group, id=request.GET.get('group_id'))
    students = group.profile_set.all().values('user__first_name', 'user__last_name')
    students_dict = {}
    f = 0
    for student in students:
        students_dict[f] = student
        f += 1
    return JsonResponse(students_dict)
