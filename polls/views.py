from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

# Las view son las encargadas de responder (con un `HttpResponse`) los
# request (`HttpRequest`). La view que se "elige" se resuelve en urls.py
# (`django.core.urlresolvers`)
# Una view tiene que retornanr un `HttpResponse` o levantar una excepcion
#
# Django provee una serie de shortcuts para acciones comunes
#
# render
# ======
#
# ```python
# context = {'latest_question_list': latest_question_list}
# return render(request, 'polls/index.html', context)
# ```
#
# es equivalente
#
# ```python
# template = loader.get_template('polls/index.html')
# context = RequestContext(request, {
#     'latest_question_list': latest_question_list,
# })
# return HttpResponse(template.render(context))
# ```
# get_object_or_404
# =================
#
# `question = get_object_or_404(Question, pk=question_id`
#
# es equivalente
#
# ```python
# try:
#     question = Question.objects.get(pk=question_id)
# except Question.DoesNotExist:
#     raise Http404('question does not exist')
# ```
#
# tambien existe `get_list_or_404` que funcion de la misma manera pero
# con `filter` en lugar de `get`


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
