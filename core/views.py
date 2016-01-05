from django.shortcuts import render
from rest_framework.response import Response
from core.models import App
from rest_framework.views import APIView

# Create your views here.
class NewApp(APIView):
    
    def post(self, request, name):
        app = App.objects.create(name=name)
        app.save()
        return Response({"id": app.key})
    

class AppList(APIView):
    
    def get(self, request):
        app_props = ['name', 'key']
        app_list = []
        apps = App.objects.all()
        for app in apps:
            new_app = {}
            for prop in app_props:
                new_app[prop] = getattr(app, prop)
            app_list.append(new_app)
        return Response({'result': app_list})