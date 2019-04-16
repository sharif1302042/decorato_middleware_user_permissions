from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponseBadRequest

ip = '192.168.1.49'

def ip_check(func):
    def wrapper(request, *args, **kwargs):
        if ip != request.META['REMOTE_ADDR']:
            return JsonResponse({'Message': 'Permission Denied'}, status=403)
        return func(request, *args, **kwargs)

    return wrapper
