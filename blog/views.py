from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Kullanici
def verigonder(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        email = request.POST.get('email')
        sifre = request.POST.get('sifre')
        telefon = request.POST.get('telefon')

        Kullanici.objects.create(ad=ad, soyad=soyad, email=email, sifre=sifre , telefon=telefon)

        return redirect('kullanicilar')
    else:
        return render(request, 'blog/form.html')
    
def kullanicilar(request):
    kullanicilar = Kullanici.objects.all()
    return render(request, 'blog/liste.html', {'kullanicilar': kullanicilar})

def sil(request, kullanici_id):
    try:
        kullanici = Kullanici.objects.get(id=kullanici_id)
        kullanici.delete()
        return redirect('kullanicilar')
    except Kullanici.DoesNotExist:
        return HttpResponse("Kullanıcı bulunamadı.", status=404)
