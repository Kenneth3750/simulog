from containerTypes.models import Containers, ContainerPalletsPosition
from pallets.models import Pallet
import json
import math
def optimize_containers(pallet_id, container_id, total_pallets):
    container = Containers.objects.get(id=container_id)
    pallet = Pallet.objects.get(id=pallet_id)
    position = ContainerPalletsPosition.objects.get(pallet_id=pallet, container_id=container)
    position1 = json.loads(position.position_1)
    total1 = position1['total']
    position2 = json.loads(position.position_2)
    total2 = position2['total']
    position3 = json.loads(position.position_3)
    total3 =  position3['total']
    max_position = max(total1, total2, total3)
    print(max_position)
    total_pallets = sum(total_pallets)
    new_total_containers = math.ceil(total_pallets / max_position)
    pallets_remaining = total_pallets % max_position
    return new_total_containers, pallets_remaining