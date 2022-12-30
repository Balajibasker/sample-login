from rest_framework import serializers 
from .models import login_data

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model =login_data
        fields ='__all__'