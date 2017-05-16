from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView
from rest_framework import viewsets
from Data.models import *
from Data.serializers import *


# Create your views here.
"""class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
"""

class HomePageView(TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
    context = super(HomePageView, self).get_context_data(**kwargs)
    context['ANGULAR_URL'] = settings.ANGULAR_URL
    return context



class DatasetViewSet(viewsets.ModelViewSet):

    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer



