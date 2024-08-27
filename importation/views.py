from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import InternationalFreightSerializer, PolicySerializer, PortOperatorSerializer
from .functions import international_freight_calculator, policy_calculator, port_operator_calculator, transship_calculator
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