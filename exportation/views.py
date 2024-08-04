from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import ExportationPriceSerializer, VolumeSerializer, WeightSerializer, InsuranceSerializer, InspectionSerializer, MobilizationManipulationSerializer
from .functions import total_volumes, total_weights, local_insurance, international_insurance, destination_insurance, origin_inspection, destination_inspection, mobilization_calculate, manipulation_calculate
import json

@api_view(['POST'])
@permission_classes([AllowAny])
def exportation_price(request):
    serializer = ExportationPriceSerializer(data=request.data)
    if serializer.is_valid():
        product_cost = serializer.validated_data['product_cost']
        package_tags_cost = serializer.validated_data['package_tags_cost']
        pallets_cost = serializer.validated_data['pallets_cost']
        other_costs = serializer.validated_data['other_costs']
        utility = serializer.validated_data['utility']
        total = product_cost + package_tags_cost + pallets_cost + other_costs + utility
        
        return Response(
            {
                'status': 'success',
                'total': total
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'status': 'error',
                'message': json.dumps(serializer.errors)
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    

@api_view(['POST'])
@permission_classes([AllowAny])
def volume(request):
    serializer = VolumeSerializer(data=request.data)
    if serializer.is_valid():
        pallet_id = serializer.validated_data['pallet_id']
        container_id = serializer.validated_data['container_id']
        number_of_pallets = serializer.validated_data['number_of_pallets']
        number_of_containers = serializer.validated_data['number_of_containers']
        total_product_volume = serializer.validated_data['total_product_volume']
        pallets_volume, containers_volume = total_volumes(pallet_id, container_id, total_product_volume, number_of_pallets, number_of_containers)
        
        return Response(
            {
                'status': 'success',
                'pallets_volume': pallets_volume,
                'containers_volume': containers_volume
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'status': 'error',
                'message': json.dumps(serializer.errors)
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['POST'])
@permission_classes([AllowAny])
def weight(request):
    serializer = WeightSerializer(data=request.data)
    if serializer.is_valid():
        pallet_id = serializer.validated_data['pallet_id']
        container_id = serializer.validated_data['container_id']
        number_of_pallets = serializer.validated_data['number_of_pallets']
        number_of_containers = serializer.validated_data['number_of_containers']
        total_product_weight = serializer.validated_data['total_product_weight']
        fee = serializer.validated_data['fee']
        pallets_weight, containers_weight, total_freight = total_weights(pallet_id, container_id, total_product_weight, number_of_pallets, number_of_containers, fee)
        
        return Response(
            {
                'status': 'success',
                'pallets_weight': pallets_weight,
                'containers_weight': containers_weight,
                'total_freight': total_freight
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'status': 'error',
                'message': json.dumps(serializer.errors)
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['POST'])
@permission_classes([AllowAny])
def insurance(request):
    serializer = InsuranceSerializer(data=request.data)
    if serializer.is_valid():
        local_fee_1 = serializer.validated_data['local_fee_1']
        local_fee_2 = serializer.validated_data['local_fee_2']
        local_value_1 = serializer.validated_data['local_value_1']
        local_value_2 = serializer.validated_data['local_value_2']
        international_fee_1 = serializer.validated_data['international_fee_1']
        international_fee_2 = serializer.validated_data['international_fee_2']
        international_value_1 = serializer.validated_data['international_value_1']
        international_value_2 = serializer.validated_data['international_value_2']
        destination_fee_1 = serializer.validated_data['destination_fee_1']
        destination_fee_2 = serializer.validated_data['destination_fee_2']
        destination_value_1 = serializer.validated_data['destination_value_1']
        destination_value_2 = serializer.validated_data['destination_value_2']
        
        local_insurance_1, local_insurance_2, best_local_option = local_insurance(local_fee_1, local_fee_2, local_value_1, local_value_2)
        international_insurance_1, international_insurance_2, best_international_option = international_insurance(international_fee_1, international_fee_2, international_value_1, international_value_2)
        destination_insurance_1, destination_insurance_2, best_destination_option = destination_insurance(destination_fee_1, destination_fee_2, destination_value_1, destination_value_2)
        
        return Response(
            {
                'status': 'success',
                'local_insurance_1': local_insurance_1,
                'local_insurance_2': local_insurance_2,
                'best_local_option': best_local_option,
                'international_insurance_1': international_insurance_1,
                'international_insurance_2': international_insurance_2,
                'best_international_option': best_international_option,
                'destination_insurance_1': destination_insurance_1,
                'destination_insurance_2': destination_insurance_2,
                'best_destination_option': best_destination_option
            },
            status=status.HTTP_200_OK
        )
    
    else:
        return Response(
            {
                'status': 'error',
                'message': json.dumps(serializer.errors)
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    

@api_view(['POST'])
@permission_classes([AllowAny])
def inspection(request):
    serializer = InspectionSerializer(data=request.data)
    if serializer.is_valid():
        origin_fee_1 = serializer.validated_data['origin_fee_1']
        origin_fee_2 = serializer.validated_data['origin_fee_2']
        origin_value_1 = serializer.validated_data['origin_value_1']
        origin_value_2 = serializer.validated_data['origin_value_2']
        destination_fee_1 = serializer.validated_data['destination_fee_1']
        destination_fee_2 = serializer.validated_data['destination_fee_2']
        destination_value_1 = serializer.validated_data['destination_value_1']
        destination_value_2 = serializer.validated_data['destination_value_2']
        
        origin_inspection_1, origin_inspection_2, best_origin_option = origin_inspection(origin_fee_1, origin_fee_2, origin_value_1, origin_value_2)
        destination_inspection_1, destination_inspection_2, best_destination_option = destination_inspection(destination_fee_1, destination_fee_2, destination_value_1, destination_value_2)
        
        return Response(
            {
                'status': 'success',
                'origin_inspection_1': origin_inspection_1,
                'origin_inspection_2': origin_inspection_2,
                'best_origin_option': best_origin_option,
                'destination_inspection_1': destination_inspection_1,
                'destination_inspection_2': destination_inspection_2,
                'best_destination_option': best_destination_option
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'status': 'error',
                'message': json.dumps(serializer.errors)
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['POST'])
@permission_classes([AllowAny])
def mobilization_and_manipulation(request):
    serializer = MobilizationManipulationSerializer(data=request.data)
    if serializer.is_valid():
        origin_mobilization_fee_1 = serializer.validated_data['origin_mobilization_fee_1']
        origin_mobilization_fee_2 = serializer.validated_data['origin_mobilization_fee_2']
        origin_mobilization_value_1 = serializer.validated_data['origin_mobilization_value_1']
        origin_mobilization_value_2 = serializer.validated_data['origin_mobilization_value_2']
        destination_mobilization_fee_1 = serializer.validated_data['destination_mobilization_fee_1']
        destination_mobilization_fee_2 = serializer.validated_data['destination_mobilization_fee_2']
        destination_mobilization_value_1 = serializer.validated_data['destination_mobilization_value_1']
        destination_mobilization_value_2 = serializer.validated_data['destination_mobilization_value_2']

        origin_manipulation_fee_1 = serializer.validated_data['origin_manipulation_fee_1']
        origin_manipulation_fee_2 = serializer.validated_data['origin_manipulation_fee_2']
        origin_manipulation_value_1 = serializer.validated_data['origin_manipulation_value_1']
        origin_manipulation_value_2 = serializer.validated_data['origin_manipulation_value_2']
        destination_manipulation_fee_1 = serializer.validated_data['destination_manipulation_fee_1']
        destination_manipulation_fee_2 = serializer.validated_data['destination_manipulation_fee_2']
        destination_manipulation_value_1 = serializer.validated_data['destination_manipulation_value_1']
        destination_manipulation_value_2 = serializer.validated_data['destination_manipulation_value_2']

        origin_mobilization_1, origin_mobilization_2, destination_mobilization_1, destination_mobilization_2, best_mobilization_origin_option, best_mobilization_destination_option = mobilization_calculate(origin_mobilization_fee_1, origin_mobilization_fee_2, origin_mobilization_value_1, origin_mobilization_value_2, destination_mobilization_fee_1, destination_mobilization_fee_2, destination_mobilization_value_1, destination_mobilization_value_2)
        origin_manipulation_1, origin_manipulation_2, destination_manipulation_1, destination_manipulation_2, best_manipulation_origin_option, best_manipulation_destination_option = manipulation_calculate(origin_manipulation_fee_1, origin_manipulation_fee_2, origin_manipulation_value_1, origin_manipulation_value_2, destination_manipulation_fee_1, destination_manipulation_fee_2, destination_manipulation_value_1, destination_manipulation_value_2)

        return Response(
            {
                'status': 'success',
                'origin_mobilization_1': origin_mobilization_1,
                'origin_mobilization_2': origin_mobilization_2,
                'destination_mobilization_1': destination_mobilization_1,
                'destination_mobilization_2': destination_mobilization_2,
                'best_mobilization_origin_option': best_mobilization_origin_option,
                'best_mobilization_destination_option': best_mobilization_destination_option,
                'origin_manipulation_1': origin_manipulation_1,
                'origin_manipulation_2': origin_manipulation_2,
                'destination_manipulation_1': destination_manipulation_1,
                'destination_manipulation_2': destination_manipulation_2,
                'best_manipulation_origin_option': best_manipulation_origin_option,
                'best_manipulation_destination_option': best_manipulation_destination_option
            }, 
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'status': 'error',
                'message': json.dumps(serializer.errors)
            },
            status=status.HTTP_400_BAD_REQUEST
        )