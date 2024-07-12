from django.shortcuts import render
from .serializers import ContainerSerializer, TotalContainerSerializer, positionContainerSerializer
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
    
@api_view(['POST'])
@permission_classes([AllowAny])
def getContainerPosition(request):
    serializer = positionContainerSerializer(data=request.data)
    
    if serializer.is_valid():
        pallet_id = serializer.data['pallet_id']
        container_id = serializer.data['container_id']
        number_of_pallets = serializer.data['number_of_pallets']
        try:
            container = Containers.objects.get(id=container_id)
            pallet = Pallet.objects.get(id=pallet_id)
            position = ContainerPalletsPosition.objects.get(pallet_id=pallet, container_id=container)
            position1 = json.loads(position.position_1)
            large1, width1, total1 = position1['large'], position1['width'], position1['total']
            position2 = json.loads(position.position_2)
            large2, width2, total2 = position2['large'], position2['width'], position2['total']
            position3 = json.loads(position.position_3)
            large3, width3, total3 = position3['large'], position3['width'], position3['total']
            max_position = max(total1, total2, total3)
            total_containers = math.ceil(number_of_pallets / max_position)
            return Response(
                {'status': 'success',
                 "large1": large1,
                 "width1": width1,
                 "total1": total1,
                 "large2": large2,
                 "width2": width2,
                 "total2": total2,
                 "large3": large3,
                 "width3": width3,
                 "total3": total3,
                 "max_position": max_position,
                 "total_containers": total_containers
                 },
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
    serializer = TotalContainerSerializer(data=request.data)
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