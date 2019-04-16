from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None

        if hasattr(self, 'process_request'):
            response = self.process_request(request)

        if not response:
            response = self.get_response(request)

        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class IPCheck(MiddlewareMixin):
    def process_request(self, request):
        return None

    def process_response(self, request, response):
        ip = '192.168.1.49'
        request_ip = request.META['REMOTE_ADDR']
        if ip == request_ip:
            return JsonResponse({'Message': 'You are ok'}, status=200)

        return JsonResponse({'Message': 'Permission Denied'}, status=403)
