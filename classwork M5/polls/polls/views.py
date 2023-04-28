from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from polls.models import Question, Choice


def homepage(request):
    return render(request, 'home.html')


def questions_list(request):
    # without templates
    # questions = Question.objects.all()
    # response = ''
    # for index, question in enumerate(questions):
    #     response += f"{index + 1}. {question.text}<br>"
    # return HttpResponse(f"Questions list here.<br>{response}")

    questions = Question.objects.all()

    context = {
        "questions": questions
    }

    return render(request, 'polls/questions.html', context=context)


def question_detail(request, question_id):
    # without template
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404
    # else:
    #     return HttpResponse(f"Question text: {question.text}<br>pub_date: {question.pub_date}")
    # question = get_object_or_404(Question, id=question_id)
    # return HttpResponse(f"Question text: {question.text}<br>pub_date: {question.pub_date}")

    question = get_object_or_404(Question, id=question_id)
    # choices = Choice.objects.filter(question=question)

    context = {
        "question": question,
        # "choices": choices
    }

    return render(request, 'polls/question_detail.html', context=context)
