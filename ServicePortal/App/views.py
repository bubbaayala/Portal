# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import App, AppDetail
from .forms import AppForm, AppDetailForm
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'App/index.html'
    context_object_name = 'all_apps'

    def get_queryset(self):
        return App.objects.all()


#def index(request):
#    all_apps = App.objects.all()
#    return render(request, 'App/index.html', {'all_apps' : all_apps})

class DetailView(generic.DetailView):
    model = App
    template_name = 'App/detail.html'
#def detail(request, app.pk):
#    app = get_object_or_404(App, pk=app_id)
#    return render(request, 'App/detail.html', {'app' : app})

class AppCreate(CreateView):
    model = App
    fields = ['app_name', 'team_name', 'status']

class AppUpdate(UpdateView):
    model = App
    fields = ['app_name', 'team_name', 'status']

class AppDelete(DeleteView):
    model = App
    success_url = reverse_lazy('App:index')


def appdetail_add(request, pk):
    app = get_object_or_404(App, pk=pk)
    if request.method == "POST":
        form = AppDetailForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.app = app
            detail.save()
            return redirect('App:detail', pk=app.pk)
    else:
        form = AppDetailForm()
    return render(request, 'App/appdetail_form.html', {'form':form})
