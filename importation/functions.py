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

def transship_calculator(fee_1, fee_2, value_1, value_2):
    total_1 = fee_1 * value_1
    total_2 = fee_2 * value_2
    best_option = min(total_1, total_2)
    return total_1, total_2, best_option