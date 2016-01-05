import datetime
from django.utils.timezone import utc
from rest_framework.views import APIView
from rest_framework import HTTP_HEADER_ENCODING
from core.models import App
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated


# A wrapper around APIView to capture miscelleneous data
# such as number of api requests as well as validate
# app id of each request
class ApiWrapper(APIView):

    # super's initial does a lot of heavy lifting
    # we log an api request after validation from APIView

    def initial(self, request, *args, **kwargs):
        super(ApiWrapper, self).initial(request, *args, **kwargs)
        self.authenticate_api_id(request)

    def authenticate_api_id(self, request):
        token = self.get_app_header(request)
        if not token:
            raise NotAuthenticated("Database ID not provided")
        try:
            app = App.objects.get(key=token)
        except App.DoesNotExist:
            # invalid app id
            raise AuthenticationFailed('Invalid Database ID.')
        
        request.META['app'] = app

    def get_app_header(self, request):
        auth = request.META.get('HTTP_APPID', b'')
        if isinstance(auth, str):
            # Work around django test client oddness
            auth = auth.encode(HTTP_HEADER_ENCODING)
        return auth
