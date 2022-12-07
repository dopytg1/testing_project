from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from .models import TestSet, Question, Answer


def test(request):
    return render(request, "base.html", {})


def test_passing(request, id, page):
    test_questions = Question.objects.filter(test_set_id=id)
    paginator = Paginator(test_questions, 1)
    
    try:
        test_questions = paginator.page(page)
        test = Question.objects.get(pk=test_questions.object_list)
        answers = Answer.objects.filter(question_id=test)
    except EmptyPage:
        test_questions = paginator.page(paginator.num_pages)

    context = {
        "id": id,
        "questions": test_questions,
        "answers": answers
    }

    return render(request, 'questions/test_passing.html', context)


def home(request):
    tests = TestSet.objects.all()

    context = {
        "tests": tests
    }

    return render(request, 'questions/index.html', context)
