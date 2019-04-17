from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import status

ip = '192.168.1.49'

def ip_check(func):
    def wrapper(request, *args, **kwargs):
        if ip != request.META['REMOTE_ADDR']:
            return JsonResponse({'Message': 'Access Denied'}, status=status.HTTP_403_FORBIDDEN)
        return func(request, *args, **kwargs)

    return wrapper
