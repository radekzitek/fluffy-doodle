# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def echo(request):
    """
    Endpoint that returns the details of the request.
    """
    response_data = {
        "method": request.method,
        "headers": dict(request.headers),
        "body": request.body.decode('utf-8'),
        "path": request.path,
        "query_params": dict(request.GET)
    }
    return HttpResponse(json.dumps(response_data, indent=4), content_type="application/json")
