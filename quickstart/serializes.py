from rest_framework.serializers import ModelSerializer
from quickstart.models import Students
class StudentsSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = ('first_name', 'last_name', 'gender', 'age')