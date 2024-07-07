from functools import wraps
from django.http import JsonResponse

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user_role = request.session.get('emp_role')
            if not user_role:
                return JsonResponse({'error': 'User not logged in'}, status=401)

            if user_role not in allowed_roles:
                return JsonResponse({'error': 'Unauthorized access'}, status=403)

            return view_func(request, *args, **kwargs)

        return wrapper
    return decorator
