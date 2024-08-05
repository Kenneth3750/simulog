from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import ExportationPriceSerializer, VolumeSerializer, WeightSerializer, InsuranceSerializer, InspectionSerializer, MobilizationManipulationSerializer, CustomsBrokerSerializer, AdministrativeSerializer
from .serializers import OtherCostsSerializer, PortFacilitySerializer, PortOperatorSerializer
from .functions import total_volumes, total_weights, local_insurance, international_insurance, destination_insurance, origin_inspection, destination_inspection, mobilization_calculate, manipulation_calculate, customs_broker_calculator, origin_administrative_costs, destination_administrative_costs
from .functions import others_advisory, others_documents, others_inspections, others_weighing, others_banks, others_documentation, others_mobilization, others_storage, others_unload, port_facility_calculator
from .functions import port_operator_calculator
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
    
@api_view(['POST'])
@permission_classes([AllowAny])
def customs_broker(request):
    serializer = CustomsBrokerSerializer(data=request.data)
    if serializer.is_valid():
        origin_agency_fee = serializer.validated_data['origin_agency_fee']
        origin_documentation_fee = serializer.validated_data['origin_documentation_fee']
        destination_agency_fee = serializer.validated_data['destination_agency_fee']
        destination_documentation_fee = serializer.validated_data['destination_documentation_fee']
        origin_agency_value = serializer.validated_data['origin_agency_value']
        origin_documentation_value = serializer.validated_data['origin_documentation_value']
        destination_agency_value = serializer.validated_data['destination_agency_value']
        destination_documentation_value = serializer.validated_data['destination_documentation_value']
        
        origin_agency, origin_documentation, destination_agency, destination_documentation, total_origin, total_destination = customs_broker_calculator(origin_agency_fee, origin_documentation_fee, destination_agency_fee, destination_documentation_fee, origin_agency_value, origin_documentation_value, destination_agency_value, destination_documentation_value)
        return Response(
            {
                'status': 'success',
                'origin_agency': origin_agency,
                'origin_documentation': origin_documentation,
                'destination_agency': destination_agency,
                'destination_documentation': destination_documentation,
                'total_origin': total_origin,
                'total_destination': total_destination
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
        mobilization_value = serializer.validated_data['mobilization_value']
        mobilization_units = serializer.validated_data['mobilization_units']
        mobilization_time = serializer.validated_data['mobilization_time']
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
        total_mobilization = others_mobilization(mobilization_value, mobilization_units, mobilization_time)
        total_bank = others_banks(bank_value, bank_units)
        total_documentation = others_documentation(documentation_value, documentation_units)
        total_unload = others_unload(unload_value, unload_units)
        total_advisory = others_advisory(advisory_value, advisory_units, advisory_time)
        total_documents = others_documents(documents_value, documents_units)
        total_inspections = others_inspections(inspections_value, inspections_units)
        total_weighing = others_weighing(weighing_value, weighing_units)
        total_others = total_documents + total_inspections + total_weighing

        return Response(
            {
                'status': 'success',
                'total_storage': total_storage,
                'total_mobilization': total_mobilization,
                'total_bank': total_bank,
                'total_documentation': total_documentation,
                'total_unload': total_unload,
                'total_advisory': total_advisory,
                'total_documents': total_documents,
                'total_inspections': total_inspections,
                'total_weighing': total_weighing,
                'total_others': total_others
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
    serializer = PortFacilitySerializer(data=request.data)
    if serializer.is_valid():
        origin_fee = serializer.validated_data['origin_fee']
        origin_value = serializer.validated_data['origin_value']
        destination_fee = serializer.validated_data['destination_fee']
        destination_value = serializer.validated_data['destination_value']
        
        origin_port_facility, destination_port_facility = port_facility_calculator(origin_fee, origin_value, destination_fee, destination_value)
        return Response(
            {
                'status': 'success',
                'origin_port_facility': origin_port_facility,
                'destination_port_facility': destination_port_facility
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
        origin_fee = serializer.validated_data['origin_fee']
        origin_value = serializer.validated_data['origin_value']
        destination_fee = serializer.validated_data['destination_fee']
        destination_value = serializer.validated_data['destination_value']
        
        origin_port_operator, destination_port_operator = port_operator_calculator(origin_fee, origin_value, destination_fee, destination_value)
        return Response(
            {
                'status': 'success',
                'origin_port_operator': origin_port_operator,
                'destination_port_operator': destination_port_operator
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
    