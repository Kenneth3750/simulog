

def containerPositions(pallet_id, container_id):
    if pallet_id == 1 and container_id == 1:
        return {
        'position_1': {
            'boxes': position_1_boxes,
            'large': large_1,
            'width': width_1,
            'height': height
        },
        'position_2': {
            'boxes': position_2_boxes,
            'large': large_2,
            'width': width_2,
            'height': height
        
        },
        'position_3': {
            'boxes': position_3_boxes,
            'large': None,
            'width': None,
            'height': height
        }
    }