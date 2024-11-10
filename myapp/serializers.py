from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(required = True, max_length = 250)
    author = serializers.CharField(required = True, max_length = 250)
    published_date = serializers.DateField()