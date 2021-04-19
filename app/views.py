import datetime


from django.http import HttpResponse, JsonResponse


def ping_response(request):
    data = {"message": "pong"}
    return JsonResponse(data)


def hello_world(request):
    now = datetime.datetime.now()
    html = "Time is {}".format(now)

    return HttpResponse(html)
