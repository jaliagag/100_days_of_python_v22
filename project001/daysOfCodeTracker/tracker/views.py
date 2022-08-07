from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from tracker.models import *
from tracker.forms import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin # block view when not logged in
from django.contrib.auth.decorators import login_required # validate identity

def home(self):
    template = loader.get_template('tracker/home.html')
    document = template.render()

    return HttpResponse(document)

def about(self):
    template = loader.get_template('tracker/about.html')
    document = template.render()
    return HttpResponse(document)

# random functions


# commits model
class View_commits(ListView):
    model = Commits

    def saludo():
        a = "hola capo, este saludo viene desde una función"
        return a

    print(saludo())
    template_name = 'tracker/commits_list.html'

class Detail_commit(DetailView):
    model = Commits
    template_name = 'tracker/commits_detail.html'

class Create_commit(LoginRequiredMixin, CreateView): # needs to be logged in
    model = Commits
    success_url = '/tracker/commits/list/'
    fields = ['title','description','author','date']

class Update_commit(LoginRequiredMixin, UpdateView):
    model = Commits
    success_url = '/tracker/commits/list/'
    fields = ['title','description','author','date']

class Delete_commit(LoginRequiredMixin, DeleteView):
    model = Commits
    success_url = '/tracker/commits/list/'

def search_commits(request):
    return render(request, 'tracker/search_commits.html')

def search_commits_action(request):
    if request.GET['title']:
        title = request.GET['title']
        results = Commits.objects.filter(title__icontains=title)
        return render(request,'tracker/search_commits_results.html',{'results':results,'title':title})
    else:
        answer = 'No se enviaron datos'
    return HttpResponse(answer)

