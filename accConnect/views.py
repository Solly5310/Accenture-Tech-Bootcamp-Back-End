from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import JSONParser
#will return an error message
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView

#response from the request
from rest_framework.response import Response
from rest_framework import status
from . models import Project,  Team, User
from . serializers import projectSerializer, teamSerializer, userSerializer




# Create your views here.

# Section is dedicated to the front end


def index(request):
    return HttpResponse("Hello, world. You're at the Accenture Connect index.")

#views are the API endpoint

class ProjectView(APIView):
    def get(self, request):
        project1 = Project.objects.all()
        serializer=projectSerializer(project1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = projectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def project_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        #pk means a primary key
        p_detail = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = projectSerializer(p_detail)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = projectSerializer(p_detail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

class TeamView(APIView):
    def get(self, request):
        team1 = Team.objects.all()
        serializer=teamSerializer(team1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = teamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def team_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        t_detail = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = teamSerializer(t_detail)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = teamSerializer(t_detail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

class UserView(APIView):
    def get(self, request):
        user1 = User.objects.all()
        serializer=userSerializer(user1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        u_detail = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = userSerializer(u_detail)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = userSerializer(u_detail, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)