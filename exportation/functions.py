from pallets.models import Pallet
from containerTypes.models import Containers

def total_volumes(pallet_id, container_id, total_product_volume, number_of_pallets, number_of_containers):
    pallet = Pallet.objects.get(id=pallet_id)
    container = Containers.objects.get(id=container_id)
    pallets_volume = pallet.volume * number_of_pallets + total_product_volume
    containers_volume = container.volume * number_of_containers + pallets_volume

    return pallets_volume, containers_volume

def total_weights(pallet_id, container_id, total_product_weight, number_of_pallets, number_of_containers, fee):
    pallet = Pallet.objects.get(id=pallet_id)
    container = Containers.objects.get(id=container_id)
    pallets_weight = pallet.weight * number_of_pallets + total_product_weight
    containers_weight = container.weight * 1000 * number_of_containers + pallets_weight
    total_freight = pallets_weight * fee

    return pallets_weight, containers_weight, total_freight
    

    
def local_insurance(local_fee_1, local_fee_2, local_value_1, local_value_2):
    local_insurance_1 = local_fee_1 * local_value_1
    local_insurance_2 = local_fee_2 * local_value_2
    best_option  = min(local_insurance_1, local_insurance_2)

    return local_insurance_1, local_insurance_2, best_option

def international_insurance(international_fee_1, international_fee_2, international_value_1, international_value_2):
    international_insurance_1 = international_fee_1 * international_value_1
    international_insurance_2 = international_fee_2 * international_value_2
    best_option  = min(international_insurance_1, international_insurance_2)

    return international_insurance_1, international_insurance_2, best_option

def destination_insurance(destination_fee_1, destination_fee_2, destination_value_1, destination_value_2):
    destination_insurance_1 = destination_fee_1 * destination_value_1
    destination_insurance_2 = destination_fee_2 * destination_value_2
    best_option  = min(destination_insurance_1, destination_insurance_2)

    return destination_insurance_1, destination_insurance_2, best_option


def origin_inspection(origin_fee_1, origin_fee_2, origin_value_1, origin_value_2):
    origin_inspection_1 = origin_fee_1 * origin_value_1
    origin_inspection_2 = origin_fee_2 * origin_value_2
    best_option  = min(origin_inspection_1, origin_inspection_2)

    return origin_inspection_1, origin_inspection_2, best_option

def destination_inspection(destination_fee_1, destination_fee_2, destination_value_1, destination_value_2):
    destination_inspection_1 = destination_fee_1 * destination_value_1
    destination_inspection_2 = destination_fee_2 * destination_value_2
    best_option  = min(destination_inspection_1, destination_inspection_2)

    return destination_inspection_1, destination_inspection_2, best_option


def mobilization_calculate(origin_mobilization_fee_1, origin_mobilization_fee_2, origin_mobilization_value_1, origin_mobilization_value_2, destination_mobilization_fee_1, destination_mobilization_fee_2, destination_mobilization_value_1, destination_mobilization_value_2):
    origin_mobilization_1 = origin_mobilization_fee_1 * origin_mobilization_value_1
    origin_mobilization_2 = origin_mobilization_fee_2 * origin_mobilization_value_2
    destination_mobilization_1 = destination_mobilization_fee_1 * destination_mobilization_value_1
    destination_mobilization_2 = destination_mobilization_fee_2 * destination_mobilization_value_2
    best_origin_option  = min(origin_mobilization_1, origin_mobilization_2)
    best_destination_option  = min(destination_mobilization_1, destination_mobilization_2)
    return origin_mobilization_1, origin_mobilization_2, destination_mobilization_1, destination_mobilization_2, best_origin_option, best_destination_option

def manipulation_calculate(origin_manipulation_fee_1, origin_manipulation_fee_2, origin_manipulation_value_1, origin_manipulation_value_2, destination_manipulation_fee_1, destination_manipulation_fee_2, destination_manipulation_value_1, destination_manipulation_value_2):
    origin_manipulation_1 = origin_manipulation_fee_1 * origin_manipulation_value_1
    origin_manipulation_2 = origin_manipulation_fee_2 * origin_manipulation_value_2
    destination_manipulation_1 = destination_manipulation_fee_1 * destination_manipulation_value_1
    destination_manipulation_2 = destination_manipulation_fee_2 * destination_manipulation_value_2
    best_origin_option  = min(origin_manipulation_1, origin_manipulation_2)
    best_destination_option =  min(destination_manipulation_1, destination_manipulation_2)
    return origin_manipulation_1, origin_manipulation_2, destination_manipulation_1, destination_manipulation_2, best_origin_option, best_destination_option

def customs_broker_calculator(origin_agency_fee, origin_documentation_fee, destination_agency_fee, destination_documentation_fee, origin_agency_value, origin_documentation_value, destination_agency_value, destination_documentation_value):
    origin_agency = origin_agency_fee * origin_agency_value
    origin_documentation = origin_documentation_fee * origin_documentation_value
    destination_agency = destination_agency_fee * destination_agency_value
    destination_documentation = destination_documentation_fee * destination_documentation_value
    total_origin = origin_agency + origin_documentation
    total_destination = destination_agency + destination_documentation
    return origin_agency, origin_documentation, destination_agency, destination_documentation, total_origin, total_destination


def origin_administrative_costs(origin_operation_employees, origin_operation_hours, origin_operation_hour_salary, origin_administrative_employees, origin_administrative_hours, origin_administrative_hour_salary, exchange_rate):
    origin_operation_cost = origin_operation_employees * origin_operation_hours * origin_operation_hour_salary
    origin_administrative_cost = origin_administrative_employees * origin_administrative_hours * origin_administrative_hour_salary
    total_origin_cost = origin_operation_cost + origin_administrative_cost

    origin_operation_cost_exchange = origin_operation_cost/exchange_rate
    origin_administrative_cost_exchange = origin_administrative_cost/exchange_rate
    total_origin_cost_exchange = total_origin_cost/exchange_rate
    return origin_operation_cost, origin_administrative_cost, total_origin_cost, origin_operation_cost_exchange, origin_administrative_cost_exchange, total_origin_cost_exchange

def destination_administrative_costs(destination_operation_employees, destination_operation_hours, destination_operation_hour_salary, destination_administrative_employees, destination_administrative_hours, destination_administrative_hour_salary, exchange_rate):
    destination_operation_cost = destination_operation_employees * destination_operation_hours * destination_operation_hour_salary
    destination_administrative_cost = destination_administrative_employees * destination_administrative_hours * destination_administrative_hour_salary
    total_destination_cost = destination_operation_cost + destination_administrative_cost

    destination_operation_cost_exchange = destination_operation_cost/exchange_rate
    destination_administrative_cost_exchange = destination_administrative_cost/exchange_rate
    total_destination_cost_exchange = total_destination_cost/exchange_rate
    return destination_operation_cost, destination_administrative_cost, total_destination_cost, destination_operation_cost_exchange, destination_administrative_cost_exchange, total_destination_cost_exchange

def others_storage(storage_value, storage_units, storage_time):
    total_storage = storage_value * storage_units * storage_time
    return total_storage
def others_mobilization(mobilization_value, mobilization_time, mobilization_units):
    total_mobilization = mobilization_value * mobilization_units * mobilization_time
    return total_mobilization
def others_banks(bank_value, bank_units):
    total_banks = bank_value * bank_units
    return total_banks
def others_documentation(documentation_value, documentation_units):
    total_documentation = documentation_value * documentation_units
    return total_documentation
def others_unload(unload_value, unload_units):
    total_unload = unload_value * unload_units
    return total_unload
def others_advisory(advisor_value, advisor_units, advisory_time):
    total_advisory = advisor_value * advisor_units * advisory_time
    return total_advisory
def others_documents(documents_value, documents_units):
    total_documents = documents_value * documents_units
    return total_documents
def others_inspections(inspection_value, inspection_units):
    total_inspections = inspection_value * inspection_units
    return total_inspections
def others_weighing(weighing_value, weighing_units):
    total_weighing = weighing_value * weighing_units
    return total_weighing


def port_facility_calculator(origin_fee, origin_value, destination_fee, destination_value):
    origin_port_facility = origin_fee * origin_value
    destination_port_facility = destination_fee * destination_value
    return origin_port_facility, destination_port_facility

def port_operator_calculator(origin_fee, origin_value, destination_fee, destination_value):
    origin_port_operator = origin_fee * origin_value
    destination_port_operator = destination_fee * destination_value
    return origin_port_operator, destination_port_operator


def international_freight_calculator(fee, amount, baf, caf, ams, bl, cs, others):
    total_basic_fee = fee * amount
    total = total_basic_fee + baf + caf + ams + bl + cs + others
    return total_basic_fee, total


def factory_cost_calculator(product_cost, exportation_preparation_cost, utility):
    total = product_cost + exportation_preparation_cost + utility
    return total
def fas_value_calculator(local_transport, local_insurance, agency, storage, documents, inspection, manipulation, mobilization, port_facility, factory_value):
    total = local_transport + local_insurance + agency + storage + documents + inspection + manipulation + mobilization + port_facility + factory_value
    return total

def fob_value_calculator(administrative_costs, customs_agency, customs_broker, fas_value):
    total = administrative_costs + customs_agency + customs_broker + fas_value
    return total

def cfr_cif_value_calculator(international_freight, international_insurance, fob_value):
    cfr_value = international_freight + fob_value
    cif_value = cfr_value + international_insurance
    return cfr_value, cif_value

def policy_calculator(fee_1, value_1, fee_2, value_2):
    total_1 = fee_1 * value_1
    total_2 = fee_2 * value_2
    best_option = min(total_1, total_2)
    return total_1, total_2, best_option









































