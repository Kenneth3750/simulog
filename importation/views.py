from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import InternationalFreightSerializer, PolicySerializer, PortOperatorSerializer, MobilizationManipulationSerializer, InspectionSerializer, CustomsBrokerSerializer
from .functions import international_freight_calculator, policy_calculator, port_operator_calculator, transship_calculator, manipulation_calculate, mobilization_calculate, inspection_calculate, port_facility_calculator, customs_broker_calculate
from .functions import total_volumes, total_weights, local_insurance, international_insurance, destination_insurance, origin_administrative_costs, destination_administrative_costs, others_advisory, others_banks, others_documentation, others_inspections, others_storage, others_unload, others_weighing, others_documents, others_tariff
from .serializers import VolumeSerializer, WeightSerializer, InsuranceSerializer, AdministrativeSerializer, OtherCostsSerializer
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
def administrative_costs(request):
    serializer = AdministrativeSerializer(data=request.data)
    if serializer.is_valid():
        origin_operation_employees = serializer.validated_data['origin_operation_employees']
        origin_operation_hours = serializer.validated_data['origin_operation_hours']
        origin_operation_hour_salary = serializer.validated_data['origin_operation_hour_salary']
        origin_administrative_employees = serializer.validated_data['origin_administrative_employees']
        origin_administrative_hours = serializer.validated_data['origin_administrative_hours']
        origin_administrative_hour_salary = serializer.validated_data['origin_administrative_hour_salary']
        destination_operation_employees = serializer.validated_data['destination_operation_employees']
        destination_operation_hours = serializer.validated_data['destination_operation_hours']
        destination_operation_hour_salary = serializer.validated_data['destination_operation_hour_salary']
        destination_administrative_employees = serializer.validated_data['destination_administrative_employees']
        destination_administrative_hours = serializer.validated_data['destination_administrative_hours']
        destination_administrative_hour_salary = serializer.validated_data['destination_administrative_hour_salary']
        exchange_rate = serializer.validated_data['exchange_rate']

        origin_operation_cost, origin_administrative_cost, total_origin_cost, origin_operation_cost_exchange, origin_administrative_cost_exchange, total_origin_cost_exchange = origin_administrative_costs(origin_operation_employees, origin_operation_hours, origin_operation_hour_salary, origin_administrative_employees, origin_administrative_hours, origin_administrative_hour_salary, exchange_rate)
        destination_operation_cost, destination_administrative_cost, total_destination_cost, destination_operation_cost_exchange, destination_administrative_cost_exchange, total_destination_cost_exchange = destination_administrative_costs(destination_operation_employees, destination_operation_hours, destination_operation_hour_salary, destination_administrative_employees, destination_administrative_hours, destination_administrative_hour_salary, exchange_rate)

        return Response(
            {
                'status': 'success',
                'origin_operation_cost': origin_operation_cost,
                'origin_administrative_cost': origin_administrative_cost,
                'total_origin_cost': total_origin_cost,
                'origin_operation_cost_exchange': origin_operation_cost_exchange,
                'origin_administrative_cost_exchange': origin_administrative_cost_exchange,
                'total_origin_cost_exchange': total_origin_cost_exchange,
                'destination_operation_cost': destination_operation_cost,
                'destination_administrative_cost': destination_administrative_cost,
                'total_destination_cost': total_destination_cost,
                'destination_operation_cost_exchange': destination_operation_cost_exchange,
                'destination_administrative_cost_exchange': destination_administrative_cost_exchange,
                'total_destination_cost_exchange': total_destination_cost_exchange
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
def other_costs(request):
    serializer = OtherCostsSerializer(data=request.data)
    if serializer.is_valid():
        storage_value = serializer.validated_data['storage_value']
        storage_units = serializer.validated_data['storage_units']
        storage_time = serializer.validated_data['storage_time']

        tariff_fee_list = serializer.validated_data['tariff_fee_list']
        tariff_value_list = serializer.validated_data['tariff_value_list']

        bank_value = serializer.validated_data['bank_value']
        bank_units = serializer.validated_data['bank_units']
        documentation_value = serializer.validated_data['documentation_value']
        documentation_units = serializer.validated_data['documentation_units']
        unload_value = serializer.validated_data['unload_value']
        unload_units = serializer.validated_data['unload_units']
        advisory_value = serializer.validated_data['advisory_value']
        advisory_units = serializer.validated_data['advisory_units']
        advisory_time = serializer.validated_data['advisory_time']
        documents_value = serializer.validated_data['documents_value']
        documents_units = serializer.validated_data['documents_units']
        inspections_value = serializer.validated_data['inspections_value']
        inspections_units = serializer.validated_data['inspections_units']
        weighing_value = serializer.validated_data['weighing_value']
        weighing_units = serializer.validated_data['weighing_units']

        total_storage = others_storage(storage_value, storage_units, storage_time)
        total_bank = others_banks(bank_value, bank_units)
        total_documentation = others_documentation(documentation_value, documentation_units)
        total_unload = others_unload(unload_value, unload_units)
        total_advisory = others_advisory(advisory_value, advisory_units, advisory_time)
        total_documents = others_documents(documents_value, documents_units)
        total_inspections = others_inspections(inspections_value, inspections_units)
        total_weighing = others_weighing(weighing_value, weighing_units)
        total_others = total_documents + total_inspections + total_weighing
        tariff_total_list = others_tariff(tariff_fee_list, tariff_value_list)

        return Response(
            {
                'status': 'success',
                'total_storage': total_storage,
                'total_bank': total_bank,
                'total_documentation': total_documentation,
                'total_unload': total_unload,
                'total_advisory': total_advisory,
                'total_documents': total_documents,
                'total_inspections': total_inspections,
                'total_weighing': total_weighing,
                'total_others': total_others,
                'tariff_total_list': tariff_total_list
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