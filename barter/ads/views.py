from django.views.generic import ListView

from django.shortcuts import render
from .models import Ad, ExchangeProposal

class Ad_ListView(ListView):
    queryset = Ad.objects.filter(is_active=True)
    paginate_by = 10
    template_name = 'ads/ads_list.html'