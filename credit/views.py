from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Client, Account, Credit
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_client_list'

    def get_queryset(self):
        return Client.objects.all()


class DetailView(generic.DetailView):
    model = Client
    template_name = 'detail.html'

