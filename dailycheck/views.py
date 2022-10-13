from urllib import request
from django.shortcuts import render
from rest_framework import viewsets, filters, generics

from .serializers import TodoSerializer
from .models import Todo
# Create your views here.


class TodoViewSet(viewsets.ViewSet):
    # if request.GET()
    queryset = Todo.objects.all().order_by('date_created')
    serializer_class = TodoSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['task']
    # get_extra_actions = []
