import math

def positions(pallet, container, box_lenght, box_width, box_height, box_weight, number_of_packages, pallet_cost):
    pallet_lenght = pallet.length * 100
    pallet_width = pallet.width * 100
    pallet_height = pallet.height * 100
    number_of_packages = number_of_packages
    if pallet.id == 1:
        pallet_max_weight = 1200
    else:
        pallet_max_weight = 1500

    container_height = container.height * 100

    box_lenght = box_lenght * 100
    box_width = box_width * 100
    box_height = box_height * 100
    box_weight = box_weight


    if (pallet_lenght < box_lenght or pallet_width < box_width or container_height < box_height):
        return None
    
    #position 1

    height = math.floor((container_height - 25 ) / box_height)

    large_1 = math.floor(pallet_lenght / box_lenght)
    width_1 = math.floor(pallet_width / box_width)


    position_1_boxes = large_1 * width_1 * height

    total_weight = position_1_boxes * box_weight

    if total_weight > pallet_max_weight:
        extra_weight = total_weight - pallet_max_weight
        extra_boxes = math.ceil( (extra_weight*100) / (box_weight*100))
        position_1_boxes = position_1_boxes - extra_boxes        


    #position 2

    large_2 = math.floor(pallet_lenght / box_width)
    width_2 = math.floor(pallet_width / box_lenght)



    position_2_boxes = large_2 * width_2 * height

    total_weight = position_2_boxes * box_weight

    if total_weight > pallet_max_weight:
        extra_weight = total_weight - pallet_max_weight
        extra_boxes = math.ceil( (extra_weight*100) / (box_weight*100))
        position_2_boxes = position_2_boxes - extra_boxes  


    #position 3
    # large_3 = large_1
    # new_pallet_width = pallet_width - box_width
    # new_large_3 = math.floor(pallet_lenght / box_width)
    # new_width_3 = math.floor(new_pallet_width / box_lenght)

    # position_312_boxes = large_3 + (new_large_3 * new_width_3)



    large_3 = large_2
    new_pallet_width = pallet_width - box_lenght
    print(new_pallet_width)
    new_large_3 = math.floor(pallet_lenght / box_lenght)
    new_width_3 = math.floor(new_pallet_width / box_width)
    print(new_large_3, new_width_3)
    if new_width_3 == 0:
        position_3_boxes = position_1_boxes
        large_3 = large_1
        width_3 = width_1
    else:
        position_3_boxes = (large_3 + (new_large_3 * new_width_3)) * height
        total_weight = position_3_boxes * box_weight
        if total_weight > pallet_max_weight:
            extra_weight = total_weight - pallet_max_weight
            extra_boxes = math.ceil( (extra_weight*100) / (box_weight*100))
            position_3_boxes = position_3_boxes - extra_boxes


    max_position = max(position_1_boxes, position_2_boxes, position_3_boxes)
    total_pallets = math.ceil(number_of_packages / max_position)
    total_pallets_cost = total_pallets * pallet_cost
    return {
  
        'boxes1': position_1_boxes,
        'large1': large_1,
        'width1': width_1,
        'height1': height,


        'boxes2': position_2_boxes,
        'large2': large_2,
        'width2': width_2,
        'height2': height,
    
        'boxes3': position_3_boxes,
        'large3': None,
        'width3': None,
        'height3': height,
        'max_position': max_position,
        'total_pallets': total_pallets,
        'total_pallets_cost': total_pallets_cost
    }

    