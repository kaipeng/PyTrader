# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404

from django.contrib.auth.decorators import login_required
from django.template import RequestContext


@login_required
def index(request):
    csrf_context = RequestContext(request)
    return render_to_response("base.html", csrf_context)
