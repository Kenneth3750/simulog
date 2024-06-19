from rest_framework import serializers



class ProductWeightSerializer(serializers.Serializer):
    product_weight = serializers.FloatField()
    number_of_products = serializers.IntegerField()
    products_per_pack = serializers.IntegerField()
    package_weight = serializers.FloatField()
