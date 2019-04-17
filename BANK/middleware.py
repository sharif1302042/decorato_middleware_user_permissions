from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse

CHECK_URL = '/accountlist/'


class IPCheck:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        ip = '192.168.1.49'
        path = request.path_info  # this return the requested url

        request_ip = request.META['REMOTE_ADDR']

        print(path, CHECK_URL)

        if path == CHECK_URL:
            if ip == request_ip:
                return None
                # return JsonResponse({'Message': 'You are ok'}, status=200)

            return JsonResponse({'Message': 'Permission Denied'}, status=403)
