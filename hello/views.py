from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# @login_required(login_url=None)
class HomeListView(ListView):
    model=LogMessage

    def get_context_data(self, **kwargs):
        context=super(HomeListView, self).get_context_data(**kwargs)
        return context

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

# @login_required(login_url="/account/login")
def log_message(request):
    if request.method=="POST":
        form=LogMessageForm(request.POST)

        if form.is_valid():
            message=form.save(commit=False)
            message.log_date=datetime.now()
            message.save()
            return redirect("home")
        
    else:
        form=LogMessageForm()
        return render(request, "hello/log_message.html", {"form":form})
