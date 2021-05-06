import datetime
import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app.models import Country

def ping_response(request):
    data = {"message": "ping pong"}
    return JsonResponse(data)


def hello_world(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)

    return HttpResponse(html)


@csrf_exempt
def add_country(request):
    data = json.loads(request.body.decode('utf-8'))
    country = data['country']
    co = Country.objects.create(name=country)
    return JsonResponse({'name': country, 'id': co.id})


def fetch_country(request):
    result = list(Country.objects.all().values('id', 'name'))
    return JsonResponse(dict(result=result))


def fetch_users(request):
    data = [['vivek', 'agarwal', 'vivek@gmail.com'],
    ['Vivek', 'Agarwal', 'agrawalvivek@yahoo.com']]
    users = [dict(first_name=item[0], last_name=item[1], email=item[2])
        for item in data
    ]

    return JsonResponse(dict(result=users))
