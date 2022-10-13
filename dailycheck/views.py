from urllib import request
from django.shortcuts import render
from rest_framework import viewsets, filters, generics

from .serializers import TodoSerializer
from .models import Todo
# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    # if request.GET()
    queryset = Todo.objects.all().order_by('date_created')
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['task']

# class TodoViewTextSearch(request, viewsets.ReadOnlyModelViewSet):
#     search_term = request.query_params["user_id"]
#     queryset = Todo.objects.filter(task__contains=search_term)
#     serializer_class = TodoSerializer


# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all().order_by('place')
#     serializer_class = ProfileSerializer