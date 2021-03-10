from rest_framework import serializers
from studentbio.models import studentdata

class studentdataserializer(serializers.ModelSerializer):
    class Meta:
        model=studentdata
        fields='__all__'
