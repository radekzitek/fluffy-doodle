from django.shortcuts import render  # noqa	F401

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator  # noqa	F401
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # noqa	F401
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


@login_required
@require_GET
def get_user_profile(request):
    user = request.user
    profile_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        # Add other profile fields as needed
    }
    return JsonResponse(profile_data, status=200)


@login_required
@csrf_exempt
@require_http_methods(["PATCH", "PUT"])
def update_user_profile(request):
    try:
        data = json.loads(request.body)
        user = request.user

        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        user.email = data.get("email", user.email)
        # Update other profile fields as needed

        user.save()
        profile_data = {
            "message": "Profile updated successfully.",
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            # Add other profile fields as needed
        }
        return JsonResponse(profile_data, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
