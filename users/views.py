from django.shortcuts import redirect, reverse, render
from django.contrib.auth.forms import UserCreationForm

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse("MotoSell:home"))
    else:
        form = UserCreationForm
    return render(response, "users/zarejestruj.html", {"form": form})
