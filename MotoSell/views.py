from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Car
from datetime import datetime


class WszystkieOpublikowaneOferty(ListView):
    model = Car
    template_name = "MotoSell/opublikowane.html"
    context_object_name = "cars"
    paginate_by = 3

    def get_queryset(self):
        return Car.objects.filter(data_publikacji__lte=datetime.today()).order_by('-data_publikacji')


class WszystkieOpublikowaneOfertyUzytkownika(ListView):
    model = Car
    template_name = "MotoSell/opublikowane_uzytkownika.html"
    context_object_name = "cars"
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Car.objects.filter(uzytkownik = user).order_by('-data_publikacji')