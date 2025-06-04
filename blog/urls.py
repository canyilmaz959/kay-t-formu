
from django.urls import path
from . import views

urlpatterns = [
    path("", views.verigonder, name="verigonder"),
    path("kullanicilar/", views.kullanicilar, name="kullanicilar"),
    path("sil/<int:kullanici_id>/", views.sil, name="sil"),
]

