from django.shortcuts import render  # noqa	F401

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json


@csrf_exempt
@require_POST
def register_user(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')

        if not username or not password or not email:
            return JsonResponse({
                "error": "Validation Error",
                "details": {
                    "username": ["This field is required."] if not username else [],
                    "password": ["This field is required."] if not password else [],
                    "email": ["This field is required."] if not email else []
                }
            }, status=400)

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return JsonResponse({
                "error": "Conflict",
                "message": "Username or email already exists."
            }, status=409)

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        return JsonResponse({
            "message": "User registered successfully",
            "username": user.username,
            "email": user.email
        }, status=201)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
