from rest_framework import serializers
def validate_positive(value):
    if value < 0:
        raise serializers.ValidationError("This value must be positive")
def validate_positive_and_zero(value):
    if value <= 0:
        raise serializers.ValidationError("This value must be positive and greater than zero")




class InternationalFreightSerializer(serializers.Serializer):
    fee = serializers.FloatField(validators=[validate_positive])
    amount = serializers.FloatField(validators=[validate_positive])
    baf = serializers.FloatField(validators=[validate_positive])
    caf = serializers.FloatField(validators=[validate_positive])
    ams = serializers.FloatField(validators=[validate_positive])
    bl = serializers.FloatField(validators=[validate_positive])
    cs = serializers.FloatField(validators=[validate_positive])
    others = serializers.FloatField(validators=[validate_positive])

class PolicySerializer(serializers.Serializer):
    number_of_products = serializers.IntegerField(validators=[validate_positive_and_zero])
    local_fee_list = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    local_value_list = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    international_fee_list = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    international_value_list = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    destination_fee_list = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    destination_value_list = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

class PortOperatorSerializer(serializers.Serializer):
    number_of_products = serializers.IntegerField(validators=[validate_positive_and_zero])
    origin_fee_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    origin_value_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    origin_fee_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    origin_value_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    destination_fee_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    destination_value_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    destination_fee_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    destination_value_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    transship_fee_1 = serializers.FloatField(validators=[validate_positive])
    transship_fee_2 = serializers.FloatField(validators=[validate_positive])
    transship_value_1 = serializers.FloatField(validators=[validate_positive])
    transship_value_2 = serializers.FloatField(validators=[validate_positive])

class PortFacilitySerializer(serializers.Serializer):
    number_of_products = serializers.IntegerField(validators=[validate_positive_and_zero])
    origin_fee_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    origin_value_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    origin_fee_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    origin_value_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    destination_fee_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    destination_value_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    destination_fee_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    destination_value_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    transship_fee_1 = serializers.FloatField(validators=[validate_positive])
    transship_fee_2 = serializers.FloatField(validators=[validate_positive])
    transship_value_1 = serializers.FloatField(validators=[validate_positive])
    transship_value_2 = serializers.FloatField(validators=[validate_positive])

class MobilizationManipulationSerializer(serializers.Serializer):
    origin_mobilization_fee_1 = serializers.FloatField(validators=[validate_positive])
    origin_mobilization_fee_2 = serializers.FloatField(validators=[validate_positive])
    origin_mobilization_value_1 = serializers.FloatField(validators=[validate_positive])
    origin_mobilization_value_2 = serializers.FloatField(validators=[validate_positive])
    destination_mobilization_fee_1 = serializers.FloatField(validators=[validate_positive])
    destination_mobilization_fee_2 = serializers.FloatField(validators=[validate_positive])
    destination_mobilization_value_1 = serializers.FloatField(validators=[validate_positive])
    destination_mobilization_value_2 = serializers.FloatField(validators=[validate_positive])

    origin_manipulation_fee_1 = serializers.FloatField(validators=[validate_positive])
    origin_manipulation_fee_2 = serializers.FloatField(validators=[validate_positive])
    origin_manipulation_value_1 = serializers.FloatField(validators=[validate_positive])
    origin_manipulation_value_2 = serializers.FloatField(validators=[validate_positive])
    destination_manipulation_fee_1 = serializers.FloatField(validators=[validate_positive])
    destination_manipulation_fee_2 = serializers.FloatField(validators=[validate_positive])
    destination_manipulation_value_1 = serializers.FloatField(validators=[validate_positive])
    destination_manipulation_value_2 = serializers.FloatField(validators=[validate_positive])

class InspectionSerializer(serializers.Serializer):
    origin_fee_1 = serializers.FloatField(validators=[validate_positive])
    origin_fee_2 = serializers.FloatField(validators=[validate_positive])
    origin_value_1 = serializers.FloatField(validators=[validate_positive])
    origin_value_2 = serializers.FloatField(validators=[validate_positive])

    destination_fee_1 = serializers.FloatField(validators=[validate_positive])
    destination_fee_2 = serializers.FloatField(validators=[validate_positive])
    destination_value_1 = serializers.FloatField(validators=[validate_positive])
    destination_value_2 = serializers.FloatField(validators=[validate_positive])

class CustomsBrokerSerializer(serializers.Serializer):
    number_of_products = serializers.IntegerField(validators=[validate_positive_and_zero])
    origin_fee_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    origin_value_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    origin_fee_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    origin_value_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    destination_fee_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    destination_value_list_1 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    destination_fee_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    destination_value_list_2 = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))

    origin_documentation = serializers.FloatField(validators=[validate_positive])
    destination_documentation = serializers.FloatField(validators=[validate_positive])



class VolumeSerializer(serializers.Serializer):
    pallet_id = serializers.IntegerField()
    container_id = serializers.IntegerField()
    number_of_pallets = serializers.IntegerField(validators=[validate_positive])
    number_of_containers = serializers.IntegerField(validators=[validate_positive])
    total_product_volume = serializers.FloatField(validators=[validate_positive])


class WeightSerializer(serializers.Serializer):
    pallet_id = serializers.IntegerField()
    container_id = serializers.IntegerField()
    number_of_pallets = serializers.IntegerField(validators=[validate_positive])
    number_of_containers = serializers.IntegerField(validators=[validate_positive])
    total_product_weight = serializers.FloatField(validators=[validate_positive])
    fee = serializers.FloatField(validators=[validate_positive])

class InsuranceSerializer(serializers.Serializer):
    local_fee_1 = serializers.FloatField(validators=[validate_positive])
    local_fee_2 = serializers.FloatField(validators=[validate_positive])
    local_value_1 = serializers.FloatField(validators=[validate_positive])
    local_value_2 = serializers.FloatField(validators=[validate_positive])

    international_fee_1 = serializers.FloatField(validators=[validate_positive])
    international_fee_2 = serializers.FloatField(validators=[validate_positive])
    international_value_1 = serializers.FloatField(validators=[validate_positive])
    international_value_2 = serializers.FloatField(validators=[validate_positive])

    destination_fee_1 = serializers.FloatField(validators=[validate_positive])
    destination_fee_2 = serializers.FloatField(validators=[validate_positive])
    destination_value_1 = serializers.FloatField(validators=[validate_positive])
    destination_value_2 = serializers.FloatField(validators=[validate_positive])

class AdministrativeSerializer(serializers.Serializer):
    origin_operation_employees = serializers.IntegerField(validators=[validate_positive])
    origin_operation_hours = serializers.IntegerField(validators=[validate_positive])
    origin_operation_hour_salary = serializers.FloatField(validators=[validate_positive])
    origin_administrative_employees = serializers.IntegerField(validators=[validate_positive])
    origin_administrative_hours = serializers.IntegerField(validators=[validate_positive])
    origin_administrative_hour_salary = serializers.FloatField(validators=[validate_positive])

    destination_operation_employees = serializers.IntegerField(validators=[validate_positive])
    destination_operation_hours = serializers.IntegerField(validators=[validate_positive])
    destination_operation_hour_salary = serializers.FloatField(validators=[validate_positive])
    destination_administrative_employees = serializers.IntegerField(validators=[validate_positive])
    destination_administrative_hours = serializers.IntegerField(validators=[validate_positive])
    destination_administrative_hour_salary = serializers.FloatField(validators=[validate_positive])


    exchange_rate = serializers.FloatField(validators=[validate_positive_and_zero])

class OtherCostsSerializer(serializers.Serializer):
    storage_value = serializers.FloatField(validators=[validate_positive])
    storage_time = serializers.IntegerField(validators=[validate_positive])
    storage_units = serializers.IntegerField(validators=[validate_positive])

    bank_value = serializers.FloatField(validators=[validate_positive])
    bank_units = serializers.IntegerField(validators=[validate_positive])

    documentation_value = serializers.FloatField(validators=[validate_positive])
    documentation_units = serializers.IntegerField(validators=[validate_positive])

    unload_value = serializers.FloatField(validators=[validate_positive])
    unload_units = serializers.IntegerField(validators=[validate_positive])

    advisory_value = serializers.FloatField(validators=[validate_positive])
    advisory_time = serializers.IntegerField(validators=[validate_positive])
    advisory_units = serializers.IntegerField(validators=[validate_positive])

    documents_value = serializers.FloatField(validators=[validate_positive])
    documents_units = serializers.IntegerField(validators=[validate_positive])

    inspections_value = serializers.FloatField(validators=[validate_positive])
    inspections_units = serializers.IntegerField(validators=[validate_positive])

    weighing_value = serializers.FloatField(validators=[validate_positive])
    weighing_units = serializers.IntegerField(validators=[validate_positive])

    tariff_fee_list = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))
    tariff_value_list = serializers.ListField(child=serializers.FloatField(validators=[validate_positive]))





