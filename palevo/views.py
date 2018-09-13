from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Group, Solution, User, Teacher, Subject, Semester


def index(request):
    return HttpResponse("Hello, world. You're at the palevo-service index.")


def search(request):
    contex = {
        'solutions': Solution.objects.all(),
    }
    return HttpResponse("Hello, world. You're at the search index.")


def solutions(request):
    contex = {
        'solutions': Solution.objects.all(),
    }
    return render(request, 'palevo/solutions.html', contex)


def solution(request, solution_id):
    solution = get_object_or_404(Solution, pk=solution_id)
    contex = {
        'solution': solution,
    }
    return render(request, 'palevo/solution.html', contex)
