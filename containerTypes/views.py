from django.shortcuts import render
from .serializers import ContainerSerializer, TotalContainerSerializaer
from .models import Containers, ContainerPalletsPosition
from pallets.models import Pallet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json
import math


@api_view(['GET'])
@permission_classes([AllowAny])
def getContainer(request, id=None):
    if id:
        try:
            container = Containers.objects.get(id=id)
            serializer = ContainerSerializer(container)
            return Response(
                {'status': 'success',
                'data': serializer.data},
                status=status.HTTP_200_OK)

        except Containers.DoesNotExist:
            return Response(
                {'status': 'error',
                'message': 'Container not found'},
                status=status.HTTP_404_NOT_FOUND)
    else:
        containers = Containers.objects.all()
        serializer = ContainerSerializer(containers, many=True)
        return Response(
            {'status': 'success',
                'data': serializer.data},
            status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def getContainerPosition(request):
    pallet_id = request.query_params.get('pallet_id')
    container_id = request.query_params.get('container_id')
    
    if pallet_id and container_id:
        try:
            container = Containers.objects.get(id=container_id)
            pallet = Pallet.objects.get(id=pallet_id)
            position = ContainerPalletsPosition.objects.get(pallet_id=pallet, container_id=container)
            position1 = json.loads(position.position_1)
            position2 = json.loads(position.position_2)
            position3 = json.loads(position.position_3)
            return Response(
                {'status': 'success',
                 'position_1': position1,
                 'position_2': position2,
                 'position_3': position3},
                status=status.HTTP_200_OK)
        except ContainerPalletsPosition.DoesNotExist:
            return Response(
                {'status': 'error',
                 'message': 'Position not found'},
                status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(
            {'status': 'error',
                'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def totalContainers(request):
    serializer = TotalContainerSerializaer(data=request.data)
    if serializer.is_valid():
        number_of_pallets = serializer.data['number_of_pallets']
        pallets_per_container = serializer.data['pallets_per_container']
        total_containers = math.ceil(number_of_pallets / pallets_per_container)
        return Response(
            {'status': 'success',
             'total_containers': total_containers},
            status=status.HTTP_200_OK)
    else:
        return Response(
            {'status': 'error',
             'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST)