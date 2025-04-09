from django.shortcuts import render
from django.http import HttpResponse

def initial(request):
    return render(request, 'quater/initial.html')

def accueil(request):
    if request.method == 'POST':
        # Logique pour créer un quartier (si nécessaire)
        return render(request, 'quater/accueil.html')
    return render(request, 'quater/accueil.html')

def maison(request):
    return render(request, 'quater/maison.html')