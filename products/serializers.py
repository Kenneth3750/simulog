from rest_framework import serializers

def greater_than_zero(value):
    if value <= 0:
        raise serializers.ValidationError('Value must be greater than zero')

class ProductWeightSerializer(serializers.Serializer):
    product_weight = serializers.FloatField(validators=[greater_than_zero])
    number_of_products = serializers.IntegerField(validators=[greater_than_zero])
    products_per_pack = serializers.IntegerField(validators=[greater_than_zero])
    package_weight = serializers.FloatField(validators=[greater_than_zero])

class TotalVolumeSerializer(serializers.Serializer):
    box_length = serializers.FloatField(validators=[greater_than_zero])
    box_width = serializers.FloatField(validators=[greater_than_zero])
    box_height = serializers.FloatField(validators=[greater_than_zero])
    number_of_packages = serializers.IntegerField(validators=[greater_than_zero])

class SumTotalVolumeSerializer(serializers.Serializer):
    volumes = serializers.ListField(child=serializers.FloatField(validators=[greater_than_zero]))


class TotalCostSerializer(serializers.Serializer):
    number_of_packages = serializers.IntegerField(validators=[greater_than_zero])
    value_per_packages = serializers.FloatField(validators=[greater_than_zero])


class SumTotalCostSerializer(serializers.Serializer):
    costs = serializers.ListField(child=serializers.FloatField(validators=[greater_than_zero]))


class TotalTagSerializer(serializers.Serializer):
    tag_per_package = serializers.IntegerField(validators=[greater_than_zero])
    tag_value = serializers.FloatField(validators=[greater_than_zero])
    number_of_packages = serializers.IntegerField(validators=[greater_than_zero])


class SumTotalTagSerializer(serializers.Serializer):
    tags = serializers.ListField(child=serializers.FloatField(validators=[greater_than_zero]))
