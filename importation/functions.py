from pallets.models import Pallet
from containerTypes.models import Containers


def international_freight_calculator(fee, amount, baf, caf, ams, bl, cs, others):
    total_basic_fee = fee * amount
    total = total_basic_fee + baf + caf + ams + bl + cs + others
    return total_basic_fee, total
