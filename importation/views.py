from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import InternationalFreightSerializer, PolicySerializer, PortOperatorSerializer, MobilizationManipulationSerializer, InspectionSerializer, CustomsBrokerSerializer
from .functions import international_freight_calculator, policy_calculator, port_operator_calculator, transship_calculator, manipulation_calculate, mobilization_calculate, inspection_calculate, port_facility_calculator, customs_broker_calculate
import json

@api_view(['POST'])
@permission_classes([AllowAny])
def international_freight(request):
    serializer = InternationalFreightSerializer(data=request.data)
    if serializer.is_valid():
        fee = serializer.validated_data['fee']
        amount = serializer.validated_data['amount']
        baf = serializer.validated_data['baf']
        caf = serializer.validated_data['caf']
        ams = serializer.validated_data['ams']
        bl = serializer.validated_data['bl']
        cs = serializer.validated_data['cs']
        others = serializer.validated_data['others']
        
        total_basic_fee, total = international_freight_calculator(fee, amount, baf, caf, ams, bl, cs, others)
        return Response(
            {
                'status': 'success',
                'total_basic_fee': total_basic_fee,
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
def policy(request):
    serializer = PolicySerializer(data=request.data)
    if serializer.is_valid():
        number_of_products = serializer.validated_data['number_of_products']
        local_fee_list = serializer.validated_data['local_fee_list']
        local_value_list = serializer.validated_data['local_value_list']
        
        international_fee_list = serializer.validated_data['international_fee_list']
        international_value_list = serializer.validated_data['international_value_list']
        
        destination_fee_list = serializer.validated_data['destination_fee_list']
        destination_value_list = serializer.validated_data['destination_value_list']
        
        local_total_list = policy_calculator(number_of_products, local_fee_list, local_value_list)
        international_total_list = policy_calculator(number_of_products, international_fee_list, international_value_list)
        destination_total_list = policy_calculator(number_of_products, destination_fee_list, destination_value_list)
        
        return Response(
            {
                'status': 'success',
                'local_total_list': local_total_list,
                'international_total_list': international_total_list,
                'destination_total_list': destination_total_list
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
def port_operator(request):
    serializer = PortOperatorSerializer(data=request.data)
    if serializer.is_valid():
        number_of_products = serializer.validated_data['number_of_products']
        origin_fee_list_1 = serializer.validated_data['origin_fee_list_1']
        origin_value_list_1 = serializer.validated_data['origin_value_list_1']
        origin_fee_list_2 = serializer.validated_data['origin_fee_list_2']
        origin_value_list_2 = serializer.validated_data['origin_value_list_2']       

        destination_fee_list_1 = serializer.validated_data['destination_fee_list_1']
        destination_value_list_1 = serializer.validated_data['destination_value_list_1']
        destination_fee_list_2 = serializer.validated_data['destination_fee_list_2']
        destination_value_list_2 = serializer.validated_data['destination_value_list_2']

        origin_total_1, origin_total_2 = port_operator_calculator(number_of_products, origin_fee_list_1, origin_value_list_1, origin_fee_list_2, origin_value_list_2)
        destination_total_1, destination_total_2 = port_operator_calculator(number_of_products, destination_fee_list_1, destination_value_list_1, destination_fee_list_2, destination_value_list_2)

        transship_fee_1 = serializer.validated_data['transship_fee_1']
        transship_value_1 = serializer.validated_data['transship_value_1']
 
        transship_fee_2 = serializer.validated_data['transship_fee_2']
        transship_value_2 = serializer.validated_data['transship_value_2']       
        transship_total_1, transship_total_2, best_transship = transship_calculator(transship_fee_1, transship_fee_2, transship_value_1, transship_value_2)

        return Response(
            {
                'status': 'success',
                'origin_total_1': origin_total_1,
                'origin_total_2': origin_total_2,
                'destination_total_1': destination_total_1,
                'destination_total_2': destination_total_2,
                'transship_total_1': transship_total_1,
                'transship_total_2': transship_total_2,
                'best_transship': best_transship
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
def port_facility(request):
    serializer = PortOperatorSerializer(data=request.data)
    if serializer.is_valid():
        number_of_products = serializer.validated_data['number_of_products']
        origin_fee_list_1 = serializer.validated_data['origin_fee_list_1']
        origin_value_list_1 = serializer.validated_data['origin_value_list_1']
        origin_fee_list_2 = serializer.validated_data['origin_fee_list_2']
        origin_value_list_2 = serializer.validated_data['origin_value_list_2']       

        destination_fee_list_1 = serializer.validated_data['destination_fee_list_1']
        destination_value_list_1 = serializer.validated_data['destination_value_list_1']
        destination_fee_list_2 = serializer.validated_data['destination_fee_list_2']
        destination_value_list_2 = serializer.validated_data['destination_value_list_2']

        origin_total_1, origin_total_2 = port_facility_calculator(number_of_products, origin_fee_list_1, origin_value_list_1, origin_fee_list_2, origin_value_list_2)
        destination_total_1, destination_total_2 = port_facility_calculator(number_of_products, destination_fee_list_1, destination_value_list_1, destination_fee_list_2, destination_value_list_2)

        transship_fee_1 = serializer.validated_data['transship_fee_1']
        transship_value_1 = serializer.validated_data['transship_value_1']
 
        transship_fee_2 = serializer.validated_data['transship_fee_2']
        transship_value_2 = serializer.validated_data['transship_value_2']       
        transship_total_1, transship_total_2, best_transship = transship_calculator(transship_fee_1, transship_fee_2, transship_value_1, transship_value_2)

        return Response(
            {
                'status': 'success',
                'origin_total_1': origin_total_1,
                'origin_total_2': origin_total_2,
                'destination_total_1': destination_total_1,
                'destination_total_2': destination_total_2,
                'transship_total_1': transship_total_1,
                'transship_total_2': transship_total_2,
                'best_transship': best_transship
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
        
        origin_inspection_1, origin_inspection_2, best_origin_option = inspection_calculate(origin_fee_1, origin_value_1, origin_fee_2, origin_value_2)
        destination_inspection_1, destination_inspection_2, best_destination_option = inspection_calculate(destination_fee_1, destination_value_1, destination_fee_2, destination_value_2)
        
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
def customs_broker(request):
    serializer = CustomsBrokerSerializer(data=request.data)
    if serializer.is_valid():
        number_of_products = serializer.validated_data['number_of_products']
        origin_fee_list_1 = serializer.validated_data['origin_fee_list_1']
        origin_value_list_1 = serializer.validated_data['origin_value_list_1']
        origin_fee_list_2 = serializer.validated_data['origin_fee_list_2']
        origin_value_list_2 = serializer.validated_data['origin_value_list_2']
        
        destination_fee_list_1 = serializer.validated_data['destination_fee_list_1']
        destination_value_list_1 = serializer.validated_data['destination_value_list_1']
        destination_fee_list_2 = serializer.validated_data['destination_fee_list_2']
        destination_value_list_2 = serializer.validated_data['destination_value_list_2']
        
        origin_documentation = serializer.validated_data['origin_documentation']
        destination_documentation = serializer.validated_data['destination_documentation']

        list_origin_1, list_origin_2, total_origin = customs_broker_calculate(origin_fee_list_1, origin_value_list_1, origin_fee_list_2, origin_value_list_2, origin_documentation)
        list_destination_1, list_destination_2, total_destination = customs_broker_calculate(destination_fee_list_1, destination_value_list_1, destination_fee_list_2, destination_value_list_2, destination_documentation)

        return Response(
            {
                'status': 'success',
                'list_origin_1': list_origin_1,
                'list_origin_2': list_origin_2,
                'total_origin': total_origin,
                'list_destination_1': list_destination_1,
                'list_destination_2': list_destination_2,
                'total_destination': total_destination,
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
        
