def allow_office_ip_only_middleware(get_response):

    def middleware(request):
        response = get_response(request)

        # https://stackoverflow.com/questions/12383540/authenticate-by-ip-address-in-django

        return response

    return middleware