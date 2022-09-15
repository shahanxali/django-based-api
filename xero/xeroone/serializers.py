# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import apimodel
 
class api(object):
    def __init__(self, name,hidden):
        self.name = name
        self.hidden = hidden

# Create a model serializer
class apiSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = apimodel
        fields = ('title', 'description')