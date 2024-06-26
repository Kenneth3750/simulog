from django.conf import settings
from django.http import JsonResponse

class SharedTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        remote_addr = request.META.get('REMOTE_ADDR')
        localhost_ips = ['127.0.0.1', '::1']

        if remote_addr in localhost_ips:
            return self.get_response(request)

        auth_header = request.headers.get('Authorization')

        if auth_header:
            try:
                token_type, token = auth_header.split(' ')

                if token_type == 'Bearer' and token == settings.SHARED_API_TOKEN:
                    return self.get_response(request)
                else:
                    return JsonResponse({'detail': 'Unauthorized'}, status=401)
            except ValueError:
                return JsonResponse({'detail': 'Invalid authorization header'}, status=401)

        return JsonResponse({'detail': 'Authorization header missing'}, status=401)
