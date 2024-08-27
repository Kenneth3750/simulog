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















