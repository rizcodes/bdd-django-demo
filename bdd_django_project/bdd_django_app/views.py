from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("INDEX PAGE")


def users(request):
    return HttpResponse("{users: [Zoe,Aygul,Gokce]}")
