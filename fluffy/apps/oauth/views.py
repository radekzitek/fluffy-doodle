from django.shortcuts import render  # noqa	F401
from django.contrib.auth import authenticate, get_user_model # noqa	F401
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings
import json
import jwt
import datetime


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
            refresh_token = generate_jwt(user)
            # In a real application, use a different method for refresh tokens
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


@csrf_exempt
@require_POST
def password_reset_request(request):
    try:
        data = json.loads(request.body)
        email = data.get("email")
        if not email:
            return JsonResponse({"error": "Email is required."}, status=400)

        try:
            user = User.objects.get(email=email)
            reset_token = get_random_string(length=32)
            user.profile.reset_token = reset_token
            user.profile.save()

            reset_url = f"{request.scheme}://{request.get_host()}/auth/password/reset/confirm/?token={reset_token}"
            send_mail(
                "Password Reset Request",
                f"Click the link to reset your password: {reset_url}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )
            return JsonResponse(
                {"message": "Password reset email sent if user exists."}, status=202
            )
        except User.DoesNotExist:
            return JsonResponse(
                {"message": "Password reset email sent if user exists."}, status=202
            )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)


@csrf_exempt
@require_POST
def password_reset_confirm(request):
    try:
        data = json.loads(request.body)
        token = data.get("token")
        new_password = data.get("new_password")
        new_password_confirm = data.get("new_password_confirm")

        if not token or not new_password or not new_password_confirm:
            return JsonResponse({"error": "All fields are required."}, status=400)

        if new_password != new_password_confirm:
            return JsonResponse({"error": "Passwords do not match."}, status=400)

        try:
            user = User.objects.get(profile__reset_token=token)
            user.set_password(new_password)
            user.profile.reset_token = ""
            user.profile.save()
            user.save()
            return JsonResponse({"message": "Password reset successful."}, status=200)
        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid token."}, status=401)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)


@csrf_exempt
@require_POST
def password_change(request):
    try:
        data = json.loads(request.body)
        old_password = data.get("old_password")
        new_password = data.get("new_password")
        new_password_confirm = data.get("new_password_confirm")

        if not old_password or not new_password or not new_password_confirm:
            return JsonResponse({"error": "All fields are required."}, status=400)

        if new_password != new_password_confirm:
            return JsonResponse({"error": "Passwords do not match."}, status=400)

        user = request.user
        if not user.check_password(old_password):
            return JsonResponse({"error": "Old password is incorrect."}, status=400)

        user.set_password(new_password)
        user.save()
        return JsonResponse({"message": "Password changed successfully."}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
