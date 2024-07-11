from django.shortcuts import render
from rest_framework import status
from .serializers import PalletsSerializer, PositionPalletsSerializer, TotalPallersSerializer, PalletCost, SumPalletCost
from rest_framework.generics import GenericAPIView
from .models import Pallet
from .functions import positions
from containerTypes.models import Containers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import math


@api_view(['GET'])
@permission_classes([AllowAny])
def getPallets(request, id=None):
    if id:
        try:
            pallet = Pallet.objects.get(id=id)
            serializer = PalletsSerializer(pallet)
            return Response(
                {'status': 'success', 
                'data': serializer.data},
                status=status.HTTP_200_OK )
        
        except Pallet.DoesNotExist:
            return Response(
                {'status': 'error', 
                'message': 'Pallet not found'},
                status=status.HTTP_404_NOT_FOUND )
    
    else:
        pallets = Pallet.objects.all()
        serializer = PalletsSerializer(pallets, many=True)
        return Response(
            {'status': 'success', 
                'data': serializer.data},
            status=status.HTTP_200_OK )
        
@api_view(['POST'])
@permission_classes([AllowAny])
def getPositions(request):
    try:
        request.data['pallet_id'] = int(request.data['pallet_id'])
        request.data['container_id'] = int(request.data['container_id'])
        request.data['box_length'] = float(request.data['box_length'])
        request.data['box_width'] = float(request.data['box_width'])
        request.data['box_height'] = float(request.data['box_height'])
        request.data['box_weight'] = float(request.data['box_weight'])
        request.data['number_of_packages'] = int(request.data['number_of_packages'])
        request.data['pallet_cost'] = float(request.data['pallet_cost'])
    except:
        return Response(
            {'status': 'error', 
                'message': 'Invalid data: Could not convert to float'},
            status=status.HTTP_400_BAD_REQUEST )
    
    serializer = PositionPalletsSerializer(data=request.data)
    if serializer.is_valid():
        pallet_id = serializer.validated_data['pallet_id']
        container_id = serializer.validated_data['container_id']
        box_length = serializer.validated_data['box_length']
        box_width = serializer.validated_data['box_width']
        box_height = serializer.validated_data['box_height']
        box_weight = serializer.validated_data['box_weight']
        number_of_packages = serializer.validated_data['number_of_packages']
        pallet_cost = serializer.validated_data['pallet_cost']
        pallet = Pallet.objects.get(id=pallet_id)
        container = Containers.objects.get(id=container_id)
        result = positions(pallet, container, box_length, box_width, box_height, box_weight, number_of_packages, pallet_cost)
        print(result)
        if result:
            return Response(
                {'status': 'success', 
                    'data': result},
                status=status.HTTP_200_OK )
        else:
            return Response(
                {'status': 'error', 
                    'message': 'The dimensions of the box are too big for the pallet or container'},
                status=status.HTTP_400_BAD_REQUEST )

    else:
        return Response(
            {'status': 'error', 
                'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST )

@api_view(['POST'])
@permission_classes([AllowAny])
def totalPallets(request):
    try:
        request.data['number_of_packages'] = float(request.data['number_of_packages'])
        request.data['boxes_per_pallet'] = float(request.data['boxes_per_pallet'])
    except:
        return Response(
            {'status': 'error', 
                'message': 'Invalid data: Could not convert to float'},
            status=status.HTTP_400_BAD_REQUEST )

    serializer = TotalPallersSerializer(data=request.data)
    if serializer.is_valid():
        number_of_packages = serializer.validated_data['number_of_packages']
        boxes_per_pallet = serializer.validated_data['boxes_per_pallet']
        total_pallets = math.ceil(number_of_packages / boxes_per_pallet)
        return Response(
            {'status': 'success', 
                'total_pallets': total_pallets},
            status=status.HTTP_200_OK )
    else:
        return Response(
            {'status': 'error', 
                'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST )
    

@api_view(['POST'])
@permission_classes([AllowAny])
def palletCost(request):
    try:
        request.data['number_of_pallets'] = float(request.data['number_of_pallets'])
        request.data['pallet_cost'] = float(request.data['pallet_cost'])
    except:
        return Response(
            {'status': 'error', 
                'message': 'Invalid data: Could not convert to float'},
            status=status.HTTP_400_BAD_REQUEST )

    serializer = PalletCost(data=request.data)
    if serializer.is_valid():
        number_of_pallets = serializer.validated_data['number_of_pallets']
        pallet_cost = serializer.validated_data['pallet_cost']
        total_cost = number_of_pallets * pallet_cost
        return Response(
            {'status': 'success', 
                'total_cost': total_cost},
            status=status.HTTP_200_OK )
    else:
        return Response(
            {'status': 'error', 
                'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST )
    
@api_view(['POST'])
@permission_classes([AllowAny])
def totalPalletCost(request):
    try:
        request.data['costs'] = [float(i) for i in request.data['costs']]
    except:
        return Response(
            {'status': 'error', 
                'message': 'Invalid data: Could not convert to float'},
            status=status.HTTP_400_BAD_REQUEST )

    serializer = SumPalletCost(data=request.data)
    if serializer.is_valid():
        costs = serializer.validated_data['costs']
        total_cost = sum(costs)
        return Response(
            {'status': 'success', 
                'total_cost': total_cost},
            status=status.HTTP_200_OK )
    else:
        return Response(
            {'status': 'error', 
                'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST )