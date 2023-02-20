from django.shortcuts import render
from rest_framework import generics
from todoapp.models import *
from todoapp.serializers import TaskSerializers


class ListView(generics.ListAPIView):  # Read
    queryset = Task.objects.all()
    serializer_class = TaskSerializers


class CreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers  # Create


class DetailView(generics.RetrieveUpdateAPIView):  # Update
    queryset = Task.objects.all()
    serializer_class = TaskSerializers


class DeleteView(generics.DestroyAPIView):  # Delete
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
