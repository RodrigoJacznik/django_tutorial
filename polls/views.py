from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

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

# Antes de cambiar a Generic view
#
# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published question (not including those set
        to be published in the future
        """
        return Question.objects.filter(
                pub_date__lte=timezone.now()
                ).order_by('-pub_date')[:5]


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Exclude any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
