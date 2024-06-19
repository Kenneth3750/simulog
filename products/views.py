from django.shortcuts import render
from rest_framework import status
from  .serializers import ProductWeightSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from math import floor


@api_view(['POST'])
@permission_classes([AllowAny])
def netWeight(request):
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

        if remaining_products == 0:
            total_net_weight = (complete_packages*unit_net_weight)
        else:
            total_net_weight = (complete_packages*unit_net_weight + (remaining_products*product_weight) + package_weight)

        return Response(
            {'status': 'success', 
            'unit_net_weight': unit_net_weight,
            'total_net_weight': total_net_weight},
            status=status.HTTP_200_OK )
    else:
        return Response(
            {'status': 'error', 
            'message': 'Invalid data'},
            status=status.HTTP_400_BAD_REQUEST )


