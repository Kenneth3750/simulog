from rest_framework import serializers


def validate_positive(value):
    if value < 0:
        raise serializers.ValidationError("This value must be positive")


class ExportationPriceSerializer(serializers.Serializer):
    product_cost = serializers.FloatField(validators=[validate_positive])
    package_tags_cost = serializers.FloatField(validators=[validate_positive])
    pallets_cost = serializers.FloatField(validators=[validate_positive])
    other_costs = serializers.FloatField(validators=[validate_positive])
    utility = serializers.FloatField(validators=[validate_positive])


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

class InspectionSerializer(serializers.Serializer):
    origin_fee_1 = serializers.FloatField(validators=[validate_positive])
    origin_fee_2 = serializers.FloatField(validators=[validate_positive])
    origin_value_1 = serializers.FloatField(validators=[validate_positive])
    origin_value_2 = serializers.FloatField(validators=[validate_positive])

    destination_fee_1 = serializers.FloatField(validators=[validate_positive])
    destination_fee_2 = serializers.FloatField(validators=[validate_positive])
    destination_value_1 = serializers.FloatField(validators=[validate_positive])
    destination_value_2 = serializers.FloatField(validators=[validate_positive])

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
