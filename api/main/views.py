from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PeopleSerializer, CarSerializer
from .models import People, Car

# Create your views here.


@api_view(['GET'])
def get_person(request):
    person = People.objects.all()
    serializer = PeopleSerializer(person, many=True)
    return Response({
        'status': 200,
        'data': serializer.data
    })


@api_view(['POST'])
def save_person(request):
    data = request.data
    serializer = PeopleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': "person is save in database"
        })
    return Response({
        'status': 400,
        'error': "something went wrong.",
        'data': serializer.errors
    })


@api_view(['POST'])
def save_car(request):
    data = request.data
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': 200,
            'data': serializer.data,
            'message': 'car is save in database'
        })
    return Response({
        'status': 400,
        'data': serializer.errors,
        'message': 'something went wrong.'
    })


@api_view(['GET'])
def get_car(request):
    car = Car.objects.all()
    serializer = CarSerializer(car, many=True)
    return Response({
        'status': 200,
        'data': serializer.data,
        'message': "success"
    })


