from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Group, Solution, User, Teacher, Subject, Semester


def index(request):
    context = {

    }
    return render(request, 'palevo/index.html', context)


def solutions(request):
    context = {
        'solutions': Solution.objects.all(),
    }
    return render(request, 'palevo/solutions.html', context)


def teachers(request):
    context = {
        'teachers': Teacher.objects.all(),
    }
    return render(request, 'palevo/teachers.html', context)


def users(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'palevo/users.html', context)


def subjects(request):
    context = {
        'subjects': Subject.objects.all(),
    }
    return render(request, 'palevo/subjects.html', context)


def groups(request):
    context = {
        'groups': Group.objects.all(),
    }
    return render(request, 'palevo/groups.html', context)


def solution(request, solution_id):
    solution = get_object_or_404(Solution, pk=solution_id)
    context = {
        'solution': solution,
    }
    return render(request, 'palevo/solution.html', context)


def teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    context = {
        'teacher': teacher,
    }
    return render(request, 'palevo/teacher.html', context)


def group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    context = {
        'group': group,
    }
    return render(request, 'palevo/group.html', context)


def subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    context = {
        'subject': subject,
    }
    return render(request, 'palevo/subject.html', context)


def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user,
    }
    return render(request, 'palevo/user.html', context)
