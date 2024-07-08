from django.shortcuts import render
from rest_framework import status
from  .serializers import ProductWeightSerializer, TotalVolumeSerializer, SumTotalVolumeSerializer, TotalCostSerializer, SumTotalCostSerializer, TotalTagSerializer, SumTotalTagSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from math import floor, ceil


@api_view(['POST'])
@permission_classes([AllowAny])
def netWeight(request):
    request.data['product_weight'] = float(request.data['product_weight'])
    request.data['number_of_products'] = float(request.data['number_of_products'])
    request.data['products_per_pack'] = float(request.data['products_per_pack'])
    request.data['package_weight'] = float(request.data['package_weight'])
    serializer = ProductWeightSerializer(data=request.data)
    if serializer.is_valid():
        product_weight = serializer.validated_data['product_weight']
        number_of_products = serializer.validated_data['number_of_products']
        products_per_pack = serializer.validated_data['products_per_pack']
        package_weight = serializer.validated_data['package_weight']
        
        unit_net_weight = (products_per_pack*product_weight + package_weight)

        number_of_packages = number_of_products/products_per_pack
        complete_packages = floor(number_of_packages)
        remaining_products = number_of_products % products_per_pack

        number_of_packages = ceil(number_of_products/products_per_pack)
        # if remaining_products == 0:
        #     total_net_weight = (complete_packages*unit_net_weight)
        # else:
        #     total_net_weight = (complete_packages*unit_net_weight + (remaining_products*product_weight) + package_weight)

        total_net_weight = (number_of_packages*unit_net_weight)
        return Response(
            {'status': 'success', 
            'unit_net_weight': unit_net_weight,
            'total_net_weight': total_net_weight,
            'number_of_packages': number_of_packages},
            status=status.HTTP_200_OK )
    else:
        return Response(
            {'status': 'error', 
            'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST )

@api_view(['POST'])
@permission_classes([AllowAny])
def totalVolumePerProduct(request):
    serializer = TotalVolumeSerializer(data=request.data)
    if serializer.is_valid():
        total_boxes = serializer.validated_data['number_of_packages']
        total_volume = total_boxes * serializer.validated_data['box_length'] * serializer.validated_data['box_width'] * serializer.validated_data['box_height']

        return Response(
            {'status': 'success', 
            'total_volume': total_volume},
            status=status.HTTP_200_OK )
    else:
        return Response(
            {'status': 'error', 
            'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST )
    
@api_view(['POST'])
@permission_classes([AllowAny])
def totalVolume(request):
    serializer = SumTotalVolumeSerializer(data=request.data)
    if serializer.is_valid():
        total_volume = sum(serializer.validated_data['volumes'])
        return Response(
            {'status': 'success', 
            'total_volume': total_volume},
            status=status.HTTP_200_OK )
    else:
        return Response(
            {'status': 'error', 
            'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST )

@api_view(['POST'])
@permission_classes([AllowAny])
def totalCostPerProduct(request):
    serializer = TotalCostSerializer(data=request.data)
    if serializer.is_valid():
        total_cost = serializer.validated_data['number_of_packages'] * serializer.validated_data['value_per_packages']
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
def totalCost(request):
    serializer = SumTotalCostSerializer(data=request.data)
    if serializer.is_valid():
        total_cost = sum(serializer.validated_data['costs'])
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
def totalTagPerProduct(request):
    serializer = TotalTagSerializer(data=request.data)
    if serializer.is_valid():
        tag_pack_value = serializer.validated_data['tag_per_package'] * serializer.validated_data['tag_value']
        total_tag = tag_pack_value * serializer.validated_data['number_of_packages']
        return Response(
            {'status': 'success', 
            "tag_package_value": tag_pack_value,
            'total_tag': total_tag},
            status=status.HTTP_200_OK )
    else:
        return Response(
            {'status': 'error', 
            'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST )
    
@api_view(['POST'])
@permission_classes([AllowAny])
def totalTag(request):
    serializer = SumTotalTagSerializer(data=request.data)
    if serializer.is_valid():
        tag_pack_values = serializer.validated_data['tags']
        total_tag = sum(tag_pack_values)
        return Response(
            {'status': 'success', 
            'total_tag': total_tag},
            status=status.HTTP_200_OK )
    else:
        return Response(
            {'status': 'error', 
            'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST )

    




