from django.http import HttpResponse

def homePage(request):
    return HttpResponse("My name is nishant")