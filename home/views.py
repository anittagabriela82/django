from django.http import HttpResponse

def home(request):
    return HttpResponse("Página inicial funcionando!")

def login(request):
    return HttpResponse("Página de login funcionando!")
