from django.http import JsonResponse


def require_authentication(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse(
                {"error": "Unauthorized", "message": "User is not authenticated."},
                status=401,
            )
        return view_func(request, *args, **kwargs)

    return _wrapped_view
