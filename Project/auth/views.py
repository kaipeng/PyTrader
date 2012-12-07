# Authentication View.

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse


from activation import activate_user
from django.http import HttpResponseRedirect, Http404

from forms import RegisterForm

def success(request):
    return render_to_response("auth/success.html", request)

def logout_success(request):
    return render_to_response("auth/logout_success.html", request)
        
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            return HttpResponseRedirect("/Project/accounts/success/")
        #else:
        #    return HttpResponse(repr(form.errors))
    else:
        form = RegisterForm()
    
    csrf_context = RequestContext(request, {'form': form, })
    return render_to_response("auth/register.html", csrf_context)

def activate(request):
    user = request.GET.get('user')
    code = request.GET.get('code')
 
    if activate_user(user, code):
        return HttpResponseRedirect("/Project/")
    else:
        raise Http404