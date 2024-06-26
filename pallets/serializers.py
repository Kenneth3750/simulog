from rest_framework import serializers
from .models import Pallet

class PalletsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    width = serializers.FloatField()
    height = serializers.FloatField()
    length = serializers.FloatField()
    weight = serializers.FloatField()
    volume = serializers.FloatField()

    class Meta:
        model = Pallet
        fields = '__all__'

class PositionPalletsSerializer(serializers.Serializer):
    pallet_id = serializers.IntegerField() # 1 for amr and 2 for eur
    container_id = serializers.IntegerField() # 1 for teu, 2 for feu, 3 for teuhb, 4 for feuhb, 5 for refeer
    box_length = serializers.FloatField()
    box_width = serializers.FloatField()  
    box_height = serializers.FloatField()
    box_weight = serializers.FloatField()

class TotalPallersSerializer(serializers.Serializer):
    number_of_packages = serializers.IntegerField()
    boxes_per_pallet = serializers.IntegerField()

class PalletCost(serializers.Serializer):
    number_of_pallets = serializers.IntegerField()
    pallet_cost = serializers.FloatField()

class SumPalletCost(serializers.Serializer):
    costs = serializers.ListField(child=serializers.FloatField())
