from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .serializers import apiSerializer
from .models import apimodel
 
# create a viewset
class apiViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = apimodel.objects.all()
     
    # specify serializer to be used
    serializer_class = apiSerializer