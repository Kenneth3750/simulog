from pallets.models import Pallet
from containerTypes.models import Containers


def international_freight_calculator(fee, amount, baf, caf, ams, bl, cs, others):
    total_basic_fee = fee * amount
    total = total_basic_fee + baf + caf + ams + bl + cs + others
    return total_basic_fee, total

def policy_calculator(number_of_products, fee_list, value_list):
    total_list = []
    iterations = number_of_products 
    for i in range(number_of_products):
        total_list.append(fee_list[i] * value_list[i])
    return total_list

def port_operator_calculator(number_of_products, fee_list_1, value_list_1, fee_list_2, value_list_2):
    total_list_1 = []
    total_list_2 = []
    for i in range(number_of_products):
        total_list_1.append(fee_list_1[i] * value_list_1[i])
        total_list_2.append(fee_list_2[i] * value_list_2[i])
    return total_list_1, total_list_2

def port_facility_calculator(number_of_products, fee_list_1, value_list_1, fee_list_2, value_list_2):
    total_list_1 = []
    total_list_2 = []
    for i in range(number_of_products):
        total_list_1.append(fee_list_1[i] * value_list_1[i])
        total_list_2.append(fee_list_2[i] * value_list_2[i])
    return total_list_1, total_list_2

def transship_calculator(fee_1, fee_2, value_1, value_2):
    total_1 = fee_1 * value_1
    total_2 = fee_2 * value_2
    best_option = min(total_1, total_2)
    return total_1, total_2, best_option


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

def inspection_calculate(fee_1, amount_1, fee_2, amount_2):
    total_1 = fee_1 * amount_1
    total_2 = fee_2 * amount_2
    best_option = min(total_1, total_2)
    return total_1, total_2, best_option

def customs_broker_calculate(fee_list_1, value_list_1, fee_list_2, value_list_2, documentation):
    total_list_1 = []
    total_list_2 = []
    for i in range(len(fee_list_1)):
        total_list_1.append(fee_list_1[i] * value_list_1[i])
        total_list_2.append(fee_list_2[i] * value_list_2[i])
    total = sum(total_list_1) + sum(total_list_2) + documentation
    return total_list_1, total_list_2, total
