from django.shortcuts import render
from django.views.generic import ListView
from .models import Car
from datetime import datetime


class WszystkieOpublikowaneOferty(ListView):
    model = Car
    template_name = "MotoSell/opublikowane.html"
    context_object_name = "cars"
    paginate_by = 3

    def get_queryset(self):
        return Car.objects.filter(data_publikacji__lte=datetime.today()).order_by('-data_publikacji')