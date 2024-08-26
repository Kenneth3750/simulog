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

