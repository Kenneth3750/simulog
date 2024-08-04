from pallets.models import Pallet
from containerTypes.models import Containers

def total_volumes(pallet_id, container_id, total_product_volume, number_of_pallets, number_of_containers):
    pallet = Pallet.objects.get(id=pallet_id)
    container = Containers.objects.get(id=container_id)
    pallets_volume = pallet.volume * number_of_pallets + total_product_volume
    containers_volume = container.volume * number_of_containers + total_product_volume

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