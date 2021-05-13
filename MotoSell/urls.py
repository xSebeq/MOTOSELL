"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'MotoSell'
urlpatterns = [
    path('', views.WszystkieOpublikowaneOferty.as_view(), name="home"),
    path('opublikowane-uzytkownika/', views.WszystkieOpublikowaneOfertyUzytkownika.as_view(), name="opublikowane-uzytkownika"),
    path('dodaj/', views.DodajOferte.as_view(), name="dodaj"),
    path('edytuj/<int:pk>', views.EdytujOferte.as_view(), name="edytuj"),
    path('usun/<int:pk>', views.UsunOferte.as_view(), name="usun"),
    path('publikuj/<int:car_id>', views.publikuj, name="publikuj"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
