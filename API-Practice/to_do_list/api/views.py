from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import mission
from .serializers import missionSerializer
# Create your views here.


@api_view(['GET'])
def Homeview(request):
    tasks = mission.objects.all()
    serializers = missionSerializer(tasks,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def DetailView(request,pk):
    tasks = mission.objects.get(pk=pk)
    serializer = missionSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateView(request):
    serializer = missionSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    

@api_view(['POST'])
def UpdateView(request , pk):
    tasks = mission.objects.get(pk=pk)
    serializer = missionSerializer(data = request.data , instance=tasks)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteView(request , pk):
    tasks = mission.objects.get(pk=pk)
    tasks.delete()
    return Response('delete successfully')