# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from questions.models import Question

def home(request):
    q = Question.objects.filter(valide=True).order_by('-date_q')
    rdict ={'questions':q}
    return render_to_response('index.html',rdict,RequestContext(request))
