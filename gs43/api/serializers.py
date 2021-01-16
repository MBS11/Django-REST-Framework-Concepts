from .models import *
from rest_framework import serializers

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Singer
        fields=['id','name','gender'] 
        
class SongSerializer(serializers.ModelSerializer):
    sungby= SingerSerializer(many=True, read_only=True)
    class Meta:
        model=Song
        fields=['id','title','singer','duration','sungby']

