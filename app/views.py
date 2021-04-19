import datetime

from django.http import HttpResponse, JsonResponse

from app.models import Country

def ping_response(request):
    data = {"message": "pong"}
    return JsonResponse(data)


def hello_world(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)

    return HttpResponse(html)

def add_country(request):
    data = request.data
    country = data['country']
    co = Country.objects.create(name=country)
    return JsonResponse({'name': country, 'id': co.id})

def fetch_country(request):
    result = list(Country.objects.all().values('id', 'name'))
    return JsonResponse(dict(result=result))
