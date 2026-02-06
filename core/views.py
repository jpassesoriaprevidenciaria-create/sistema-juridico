from django.http import HttpResponse

def home(request):
    return HttpResponse('Sistema Jurídico OK')
