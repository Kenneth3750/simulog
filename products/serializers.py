from rest_framework import serializers



class ProductWeightSerializer(serializers.Serializer):
    product_weight = serializers.FloatField()
    number_of_products = serializers.IntegerField()
    products_per_pack = serializers.IntegerField()
    package_weight = serializers.FloatField()

class TotalVolumeSerializer(serializers.Serializer):
    box_length = serializers.FloatField()
    box_width = serializers.FloatField()
    box_height = serializers.FloatField()
    number_of_packages = serializers.IntegerField()

class SumTotalVolumeSerializer(serializers.Serializer):
    volumes = serializers.ListField(child=serializers.FloatField())


class TotalCostSerializer(serializers.Serializer):
    number_of_packages = serializers.IntegerField()
    value_per_packages = serializers.FloatField()


class SumTotalCostSerializer(serializers.Serializer):
    costs = serializers.ListField(child=serializers.FloatField())


class TotalTagSerializer(serializers.Serializer):
    tag_per_package = serializers.IntegerField()
    tag_value = serializers.FloatField()
    number_of_packages = serializers.IntegerField()


class SumTotalTagSerializer(serializers.Serializer):
    tags = serializers.ListField(child=serializers.FloatField())