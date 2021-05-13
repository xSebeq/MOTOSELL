from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Car
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


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


class DodajOferte(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['tytul', 'opis', 'kategoria', 'marka', 'model', 'rok_produkcji', 'przebieg', 'pojemnosc_skokowa', 'moc', 'rodzaj_paliwa', 'zdjecie', 'data_dodania', 'data_publikacji']
    template_name = "MotoSell/dodaj.html"

    def get_success_url(self):
        return reverse('MotoSell:home')

    def form_valid(self, form):
        form.instance.uzytkownik = self.request.user
        return super().form_valid(form)


class EdytujOferte(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    fields = ['tytul', 'opis', 'kategoria', 'marka', 'model', 'rok_produkcji', 'przebieg', 'pojemnosc_skokowa', 'moc', 'rodzaj_paliwa', 'zdjecie', 'data_dodania', 'data_publikacji']
    template_name = "MotoSell/edytuj.html"

    def form_valid(self, form):
        form.instance.uzytkownik = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('MotoSell:opublikowane-uzytkownika')

    def test_func(self):
        car = self.get_object()
        if self.request.user == car.uzytkownik:
            return True
        return False


def publikuj(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.user == car.uzytkownik:
        car.data_publikacji = datetime.today()
        car.save()
    return reverse_lazy('MotoSell:opublikowane-uzytkownika')


class UsunOferte(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    success_url = reverse_lazy('MotoSell:home')

    def test_func(self):
        car = self.get_object()
        if self.request.user == car.uzytkownik:
            return True
        return False
