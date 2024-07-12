from rest_framework import serializers
from .models import Pallet

def greater_than_zero(value):
    if value <= 0:
        raise serializers.ValidationError('Value must be greater than zero')

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
    box_length = serializers.FloatField(validators=[greater_than_zero])
    box_width = serializers.FloatField(validators=[greater_than_zero])  
    box_height = serializers.FloatField(validators=[greater_than_zero])
    box_weight = serializers.FloatField(validators=[greater_than_zero])
    number_of_packages = serializers.IntegerField(validators=[greater_than_zero])
    pallet_cost = serializers.FloatField(validators=[greater_than_zero])

class TotalPallersSerializer(serializers.Serializer):
    number_of_packages = serializers.IntegerField(validators=[greater_than_zero])
    boxes_per_pallet = serializers.IntegerField(validators=[greater_than_zero])

class PalletCost(serializers.Serializer):
    number_of_pallets = serializers.IntegerField(validators=[greater_than_zero])
    pallet_cost = serializers.FloatField(validators=[greater_than_zero])

class SumPalletCost(serializers.Serializer):
    costs = serializers.ListField(child=serializers.FloatField(validators=[greater_than_zero]))
