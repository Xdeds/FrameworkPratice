from quickstart.models import Students
from quickstart.serializes import StudentsSerializer
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.

# class StudentsView(APIView):
#     def get(self, request):
#         lst = Students.objects.all().values()
#         return Response({'students':list(lst)})
    
#     def post(self, request):
#         post_new = Students.objects.create(
#         first_name = request.data['first_name'],
#         last_name = request.data['last_name'],
#         gender = request.data['gender'],
#         age = request.data['age'])

#         return Response({'post':model_to_dict(post_new)})

class StudentsListView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentsCreateView(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentsRetriveView(generics.RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentsUpdateView(generics.UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentsDeleteView(generics.DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer