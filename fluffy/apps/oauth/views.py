# from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import jwt
import datetime
from django.conf import settings

SECRET_KEY = settings.SECRET_KEY


def generate_jwt(user):
    payload = {
        "user_id": user.id,
        "username": user.username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


@csrf_exempt
@require_POST
def login(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            access_token = generate_jwt(user)
            refresh_token = generate_jwt(
                user
            )  # In a real application, use a different method for refresh tokens
            return JsonResponse(
                {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "token_type": "bearer",
                    "expires_in": 3600,
                },
                status=200,
            )
        else:
            return JsonResponse(
                {"error": "Unauthorized", "message": "Invalid credentials."}, status=401
            )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)


@csrf_exempt
@require_POST
def logout(request):
    # In a real application, you would handle token revocation here
    return JsonResponse({"message": "Logged out successfully."}, status=200)


@csrf_exempt
@require_POST
def refresh_token(request):
    try:
        data = json.loads(request.body)
        refresh_token = data.get("refresh_token")
        try:
            payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])
            new_access_token = generate_jwt(user)
            return JsonResponse(
                {
                    "access_token": new_access_token,
                    "token_type": "bearer",
                    "expires_in": 3600,
                },
                status=200,
            )
        except jwt.ExpiredSignatureError:
            return JsonResponse(
                {"error": "Unauthorized", "message": "Refresh token has expired."},
                status=401,
            )
        except jwt.InvalidTokenError:
            return JsonResponse(
                {"error": "Unauthorized", "message": "Invalid refresh token."},
                status=401,
            )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
