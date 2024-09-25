from rest_framework import serializers
from .models import Containers

def greater_than_zero(value):
    if value <= 0:
        raise serializers.ValidationError('Value must be greater than zero')


class ContainerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    width = serializers.FloatField()
    height = serializers.FloatField()
    length = serializers.FloatField()
    weight = serializers.FloatField()
    volume = serializers.FloatField()


    class Meta:
        model = Containers
        fields = '__all__'

class TotalContainerSerializer(serializers.Serializer):
    pallet_id = serializers.IntegerField(validators=[greater_than_zero])
    container_id = serializers.IntegerField(validators=[greater_than_zero])
    total_pallets = serializers.ListField(child=serializers.IntegerField(validators=[greater_than_zero]))
    products_per_pallet = serializers.ListField(child=serializers.IntegerField(validators=[greater_than_zero]))


class positionContainerSerializer(serializers.Serializer):
    pallet_id = serializers.IntegerField()
    container_id = serializers.IntegerField()
    number_of_pallets = serializers.IntegerField(validators=[greater_than_zero])