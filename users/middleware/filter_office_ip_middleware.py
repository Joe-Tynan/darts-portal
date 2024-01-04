from django.conf import settings

class FilterOfficeIPMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        allowed_ips = ['81.143.193.132', '80.252.123.2']
        ip = request.META.get('REMOTE_ADDR')

        if ip not in allowed_ips:
            settings.LOCKDOWN_ENABLED=True
        else:
            settings.LOCKDOWN_ENABLED=False