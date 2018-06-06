# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

class App(models.Model):
    app_name = models.CharField(max_length = 50)
    team_name = models.CharField(max_length = 50)
    status = models.CharField(max_length = 200)

    def get_absolute_url(self):
        return reverse('App:detail', kwargs={'pk':self.pk})


    def __str__(self):
        return self.app_name + " - " + self.team_name

class AppDetail(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    team_manager_email = models.CharField(max_length = 50)
    repo_link = models.CharField(max_length = 150)
    is_secure = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('App:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.repo_link
