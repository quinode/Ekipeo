# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from questions.models import Question

def detail(request,slug):
    q = Question.objects.get(slug=slug)
    rdict ={'q':q}
    return render_to_response('detail.html',rdict,RequestContext(request))
    