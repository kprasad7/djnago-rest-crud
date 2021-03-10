from rest_framework import serializers
from .models import File
class File_for_Serializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'remark', 'timestamp')