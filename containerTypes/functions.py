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
    return new_total_containers, pallets_remaining, max_position


def palletsUniquePerContainer(containers, total_pallets, max_position, products_per_pallet):
    containers_matrix = [[0 for _ in range(len(total_pallets))] for _ in range(containers)]
    for i in range(containers):
        pallets_remaining_on_container = max_position
        for j in range(len(total_pallets)):
            if pallets_remaining_on_container == 0:
                break
            if total_pallets[j] >= pallets_remaining_on_container:
                containers_matrix[i][j] = pallets_remaining_on_container * products_per_pallet[j]
                total_pallets[j] = total_pallets[j] - pallets_remaining_on_container
                pallets_remaining_on_container = 0
            elif total_pallets[j] < pallets_remaining_on_container:
                containers_matrix[i][j] = total_pallets[j] * products_per_pallet[j]
                pallets_remaining_on_container -= total_pallets[j]
                total_pallets[j] = 0
    print(containers_matrix)
    return containers_matrix
