from django.shortcuts import render
from quickstart.models import Students
from rest_framework.response import Response

from rest_framework.views import APIView
# Create your views here.

class StudentsView(APIView):
    def get(self, request):
        lst = Students.objects.all().values()
        return Response({'students':list(lst)})